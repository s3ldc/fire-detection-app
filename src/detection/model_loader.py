# src/detection/model_loader.py

import os
from ultralytics import YOLO

MODEL_PATH = os.path.join("models", "fire_yolov8.pt")

_model_cache = None

def load_model():
    """
    Load and cache the YOLO fire detection model.
    """
    global _model_cache

    if _model_cache is None:
        print(f"Loading YOLO model from {MODEL_PATH} ...")
        _model_cache = YOLO(MODEL_PATH)
        print("YOLO model loaded successfully.")

    return _model_cache
