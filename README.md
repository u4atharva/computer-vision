<div align="center">
  <h1>👁️ Computer Vision Sandbox</h1>
  <p><i>A dedicated repository for exploring, building, and evaluating Computer Vision projects.</i></p>

  [![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-red.svg?logo=opencv&style=for-the-badge)](https://opencv.org/)
  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&style=for-the-badge)](https://www.python.org/)
</div>

---

## 📂 Current Projects

### 1. Rubik's Cube Color Calibration (`SolveCube`)
An OpenCV-based interactive utility designed to process images of a Rubik's Cube.
- **Goal**: Tune and extract exact face colors dynamically using HSV masking before feeding the data into an automated solver algorithm.
- **Techniques Used**: Real-time HSV Color Thresholding, Image manipulation, GUI trackbar listeners.

### 2. Kociemba Algorithm Integration (`KociembaDemo`)
A demonstration environment for the Kociemba's two-phase algorithm. This provides the mathematical backbone for deciphering a Rubik's cube from any state in a near-optimal number of moves. Intended to be used in tandem with the physical face color extraction process.

---

## 🛠️ Getting Started

**Prerequisites**:
Ensure you have Python installed along with `opencv-python`:

```bash
pip install opencv-python
```

**Running the Interactive Masker:**
Navigate to `SolveCube` and run the vision script:
```bash
cd ServeCube
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