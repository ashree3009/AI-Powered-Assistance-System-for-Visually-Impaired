# AI-Powered Assistance System for Visually Impaired

An AI-powered assistance system built using Python, OpenCV, and YOLOv8 to help visually impaired users by detecting surrounding objects and providing real-time audio feedback. The project combines computer vision and audio processing for accessibility-focused interaction.

---

## Features

* Real-time object detection using YOLOv8
* Audio-based environmental feedback
* Live sound detection support
* Accessibility-focused AI solution

---

## Tech Stack

* Python 3.11
* OpenCV
* YOLOv8
* NumPy
* Audio Processing Libraries

---

## Project Structure

```bash
assistive_ai_system/
│
├── audio/
│   └── yamnet_live_detection.py
│
├── vision/
│   ├── object_detection.py
│   ├── yolov8n.pt
│
├── main_system.py
├── yolov8n.pt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repo-link>
cd assistive_ai_system
```

### 2. Install Required Libraries

```bash
pip install opencv-python ultralytics numpy
```

---

## Run the Project

```bash
python main_system.py
```

The system starts real-time object and audio detection and provides voice-based feedback.

---

## Python Version

This project was developed using **Python 3.11**.

---

## Future Improvements

* Better object detection accuracy
* Mobile application support
* Multilingual voice feedback
* Edge AI deployment

---

## Author

**Shree Singal**
