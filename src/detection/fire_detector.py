# src/detection/fire_detector.py

from .model_loader import load_model

# Config
FIRE_CLASS_NAME = "fire"      # Adjust if your model uses something else
FIRE_CONF_THRESHOLD = 0.5     # Confidence threshold (tune as needed)

def detect_fire_on_frame(frame_bgr):
    """
    Run YOLO fire detection on a single frame.

    Args:
        frame_bgr: OpenCV frame in BGR format (as read from cv2).

    Returns:
        annotated_frame_bgr: frame with boxes drawn (BGR)
        fire_detected: bool, True if fire found above threshold
        max_conf: float, highest confidence for fire in this frame (0.0 if none)
    """
    model = load_model()

    # YOLO expects images in RGB, but ultralytics will handle conversion internally
    # even with BGR ndarray, so we can pass frame as is.

    results = model.predict(
        source=frame_bgr,
        verbose=False
    )

    fire_detected = False
    max_conf = 0.0

    annotated_frame = frame_bgr.copy()

    if not results:
        return annotated_frame, fire_detected, max_conf

    result = results[0]

    boxes = result.boxes  # bounding boxes

    # model.names is a dict: {class_id: "classname"}
    class_names = result.names

    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            class_name = class_names.get(cls_id, str(cls_id))

            if class_name.lower() == FIRE_CLASS_NAME.lower() and conf >= FIRE_CONF_THRESHOLD:
                fire_detected = True
                if conf > max_conf:
                    max_conf = conf

                # Get box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw rectangle and label using OpenCV
                import cv2
                label = f"{class_name.upper()} {conf:.2f}"
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(
                    annotated_frame,
                    label,
                    (x1, max(y1 - 10, 0)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2
                )

    return annotated_frame, fire_detected, max_conf
