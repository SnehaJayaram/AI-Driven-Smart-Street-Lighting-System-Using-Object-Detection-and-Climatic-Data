"""
Main Script: Smart AI Street Lighting System

- Captures video stream
- Runs object detection
- Sends command to NodeMCU
- Receives telemetry
"""

from detection import detect_objects
from comms import send_command, receive_data
import cv2

# Initialize camera
cap = cv2.VideoCapture(0)

print("System Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    # Run detection
    detected = detect_objects(frame)

    # Decision logic
    if detected:
        send_command("DETECTED")
    else:
        send_command("CLEAR")

    # Receive telemetry from NodeMCU
    data = receive_data()
    if data:
        print("Telemetry:", data)

    # Display frame (optional)
    cv2.imshow("Street View", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()