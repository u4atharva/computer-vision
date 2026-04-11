<div align="center">
  <h1>👁️ Computer Vision Sandbox</h1>
  <p><i>A dedicated repository for exploring, building, and evaluating Computer Vision projects.</i></p>

  [![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-red.svg?logo=opencv&style=for-the-badge)](https://opencv.org/)
  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&style=for-the-badge)](https://www.python.org/)
</div>


---

## 📂 Current Projects

### 1. Virtual Air Canvas (`VirtualCanvas`)
An interactive drawing application that uses your webcam to track your hand and draw lines directly on the screen! 
- **Goal**: Let users paint in thin air by tracking the tip of their index finger. Top of the screen holds colors to switch between.
- **Techniques Used**: MediaPipe Hand Landmarks (`hands.process`), OpenCV Drawing Utils, Queues to track line coordinates.

### 2. Rubik's Cube Color Calibration (`SolveCube`)
An OpenCV-based interactive utility designed to process images of a Rubik's Cube.
- **Goal**: Tune and extract exact face colors dynamically using HSV masking before feeding the data into an automated solver algorithm.
- **Techniques Used**: Real-time HSV Color Thresholding, Image manipulation, GUI trackbar listeners.

### 3. Kociemba Algorithm Integration (`KociembaDemo`)
A demonstration environment for the Kociemba's two-phase algorithm. This provides the mathematical backbone for deciphering a Rubik's cube from any state in a near-optimal number of moves. Intended to be used in tandem with the physical face color extraction process.

---

## 🛠️ Getting Started

**Prerequisites**:
Ensure you have Python installed along with `opencv-python`:

```bash
pip install -r requirements.txt
# (installs opencv-python, mediapipe, etc)
```

**1. Running Virtual Air Canvas:**
Navigate to `VirtualCanvas` and start the script.
```bash
cd VirtualCanvas
python air_canvas.py
```
>**How to use**: The boxes at the top of the video feed act as virtual buttons. 
>- **To Draw/Select**: Extend your index finger at the camera.
>- **To Pause Drawing**: Make a closed fist (fold your index finger in) to move your hand around without leaving messy strokes.
>- **Colors & Eraser**: Hover your extended finger over "BLUE", "GREEN", "RED", or "YELLOW" to switch brush colors. Hover over "CLEAR" to instantly erase your canvas.
>- **To Exit App**: Show the "Shaka" / "Call Me" sign (only thumb and pinky extended upwards) and **hold it continuously for 2 seconds**. A live timer will notify you on-screen before it safely shuts down.

>**Troubleshooting Camera (macOS)**: If the script instantly crashes and logs an `OpenCV: camera failed to properly initialize` error, macOS strict security is blocking webcam access! To fix this, open **System Settings > Privacy & Security > Camera** on your Mac and ensure that your IDE (like PyCharm) or Terminal is toggled **ON**.

**2. Running the Interactive Masker (Rubik's):**
Navigate to `SolveCube` and run the vision script:
```bash
cd SolveCube
python ProcessFace.py
```

---

## 🚀 Vision Scope
This repository will serve as the central hub for any future implementations involving:
- Object Detection and Tracking 
- Image Segmentation 
- Optical Character Recognition (OCR) 
- Facial Recognition

<br>

<p align="center">
  <i>Building machines that can see.</i>
</p>
