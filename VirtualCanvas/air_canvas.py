import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# holding the points drawn by the user for different colors
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

# keeping track of the current line index
b_idx, g_idx, r_idx, y_idx = 0, 0, 0, 0

# bgr values for the colors we want
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# a blank white canvas to draw on as a separate window
canvas = np.zeros((471, 636, 3)) + 255

# setup mediapipe for hand tracking
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # flip the frame so it acts like a mirror
    frame = cv2.flip(frame, 1)
    
    # create the color selection boxes at the top of the frame
    frame = cv2.rectangle(frame, (40, 1), (140, 65), (0,0,0), 2)
    frame = cv2.rectangle(frame, (160, 1), (255, 65), (255,0,0), 2)
    frame = cv2.rectangle(frame, (275, 1), (370, 65), (0,255,0), 2)
    frame = cv2.rectangle(frame, (390, 1), (485, 65), (0,0,255), 2)
    frame = cv2.rectangle(frame, (505, 1), (600, 65), (0,255,255), 2)
    
    # put text in the boxes so we know what they do
    cv2.putText(frame, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 2, cv2.LINE_AA)
    
    # convert to rgb for mediapipe to process
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # get hand landmarks
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for handLM in result.multi_hand_landmarks:
            
            lm_list = []
            for id, lm in enumerate(handLM.landmark):
                h, w, c = frame.shape
                # getting x and y coords of landmarks
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                
            if len(lm_list) != 0:
                # index finger tip is landmark id 8
                x1, y1 = lm_list[8][1], lm_list[8][2]
                
                # check if index finger is open (tip is higher than pip joint)
                is_index_open = lm_list[8][2] < lm_list[6][2]
                
                if is_index_open:
                    # if finger is at the top of the screen where buttons are
                    if y1 <= 65:
                        if 40 <= x1 <= 140: # hit clear button
                            bpoints = [deque(maxlen=512)]
                            gpoints = [deque(maxlen=512)]
                            rpoints = [deque(maxlen=512)]
                            ypoints = [deque(maxlen=512)]
                            b_idx, g_idx, r_idx, y_idx = 0, 0, 0, 0
                            canvas[67:, :, :] = 255 
                        elif 160 <= x1 <= 255: colorIndex = 0
                        elif 275 <= x1 <= 370: colorIndex = 1
                        elif 390 <= x1 <= 485: colorIndex = 2
                        elif 505 <= x1 <= 600: colorIndex = 3
                    else:
                        # just drawing
                        if colorIndex == 0:
                            bpoints[b_idx].appendleft((x1, y1))
                        elif colorIndex == 1:
                            gpoints[g_idx].appendleft((x1, y1))
                        elif colorIndex == 2:
                            rpoints[r_idx].appendleft((x1, y1))
                        elif colorIndex == 3:
                            ypoints[y_idx].appendleft((x1, y1))
                else:
                    # fist is closed (index finger not open), dont draw
                    bpoints.append(deque(maxlen=512))
                    b_idx += 1
                    gpoints.append(deque(maxlen=512))
                    g_idx += 1
                    rpoints.append(deque(maxlen=512))
                    r_idx += 1
                    ypoints.append(deque(maxlen=512))
                    y_idx += 1
                        
            # draw the landmarks on the video frame
            mpDraw.draw_landmarks(frame, handLM, mpHands.HAND_CONNECTIONS)
            
    else:
        # no hand seen, append empty deque to break the line drawing
        bpoints.append(deque(maxlen=512))
        b_idx += 1
        gpoints.append(deque(maxlen=512))
        g_idx += 1
        rpoints.append(deque(maxlen=512))
        r_idx += 1
        ypoints.append(deque(maxlen=512))
        y_idx += 1
        
    # draw all the lines from the points arrays
    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                # draw the lines on both original frame and canvas
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(canvas, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                
    # show the windows
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint Canvas", canvas)
    
    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
