"""
Detection Module

Uses YOLO model to detect:
- Cars
- People
"""

from ultralytics import YOLO

# Load YOLO model (use your trained model or yolov8n.pt)
model = YOLO("yolov8n.pt")

# Classes of interest
TARGET_CLASSES = ["person", "car", "motorbike", "bus", "truck"]


def detect_objects(frame):
    """
    Returns True if relevant object detected
    """

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label in TARGET_CLASSES:
                return True

    return False