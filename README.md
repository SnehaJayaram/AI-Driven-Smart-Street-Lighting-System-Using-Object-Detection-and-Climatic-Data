# Smart AI-Based Street Lighting System

## 📌 Overview
This project presents an intelligent street lighting system that uses AI-based object detection to control street lights efficiently. The system reduces energy consumption by activating lights only when vehicles or pedestrians are detected.

## ⚙️ Features
- AI-based object detection using YOLO
- Real-time video processing with OpenCV
- Automatic light control based on movement
- MQTT communication between Raspberry Pi and NodeMCU
- Environment-based adjustments using sensors (LDR, DHT11)

## 🛠️ Technologies Used
- Python
- YOLO (Ultralytics)
- OpenCV
- MQTT Protocol
- Embedded Systems (NodeMCU, Raspberry Pi)

## 🧠 Working Principle
1. Camera captures real-time video.
2. Raspberry Pi processes frames using YOLO.
3. If an object is detected → command sent via MQTT.
4. NodeMCU receives signal and controls street light.
5. Sensors adjust brightness based on environment.

## 📂 Project Structure