# Fire Detection System (Python + YOLOv8)

A real-time fire detection application built using Python, OpenCV, and YOLOv8. The system opens your webcam, detects fire in real time, draws bounding boxes, and plays an alert sound when fire is detected.

## Features
- Real-time fire detection (YOLOv8)
- Webcam live feed
- Bounding boxes on fire regions
- Alert sound on detection
- Simple Tkinter user interface
- Easy to replace model weights

## Tech Stack
Python, YOLOv8, OpenCV, Tkinter, Pillow, Pygame

## Project Structure
fire-detection-app/
├── assets/alert_sound.mp3
├── models/fire_yolov8.pt
├── src/
│   ├── app.py
│   ├── ui/
│   ├── detection/
│   └── utils/
└── requirements.txt

## Installation
pip install -r requirements.txt

Place your model at: models/fire_yolov8.pt  
Place your alert sound at: assets/alert_sound.mp3

## Run the App
python src/app.py

## Notes
- Adjust detection confidence in fire_detector.py
- Replace YOLO model anytime
- Works offline

## Author
Sunil Biriya
