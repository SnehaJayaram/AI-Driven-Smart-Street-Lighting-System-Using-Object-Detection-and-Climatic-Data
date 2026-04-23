# 💡 AI-Driven Smart Street Lighting System
### Using Object Detection and Climatic Data

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Arduino](https://img.shields.io/badge/Hardware-Arduino%20Uno-00979D.svg)](https://www.arduino.cc/)
[![YOLOv8](https://img.shields.io/badge/AI-Object%20Detection-red.svg)](#)

## 🎯 Project Objective
Urban street lighting often runs at 100% capacity even when streets are empty or during bright moonlit nights, leading to massive energy wastage. This project introduces a **Context-Aware Lighting System** that adjusts brightness based on two primary inputs:
1. **Human/Vehicle Presence:** Detected via real-time computer vision.
2. **Climatic Conditions:** Ambient light (LDR) and weather data to adjust for fog, rain, or clear nights.

---

## 📊 System Architecture & Results
### 1. Object Detection in Action
![Detection Result](./assets/object_detection_sample.png)
*Figure 1: The system identifying pedestrians and vehicles to trigger "Active Lighting" mode.*

### 2. Hardware Prototype
![Hardware Setup](./assets/hardware_prototype.jpg)
*Figure 2: The integrated Arduino circuit with LDR, PIR, and LED modules.*

---

## 🧠 How it Works
- **The Vision Layer:** Uses a pre-trained **YOLO (You Only Look Once)** model to identify "Road Users." If the street is empty, the lights dim to 10% to save power.
- **The Climatic Layer:** LDR sensors monitor lux levels. If climatic data indicates heavy fog or rain, the system increases brightness even if no objects are detected, ensuring safety.
- **The Integration:** A Python script bridges the AI model with the **Arduino Uno** via Serial Communication, sending real-time dimming commands.

## 👥 Team & Collaboration
This project was a collaborative effort by a **group of 4 members**. My technical focus included:
- **AI-Hardware Bridge:** Developed the Python-to-Arduino communication protocol (PySerial).
- **Vision Integration:** Implementing the Object Detection logic and defining threshold levels for light activation.
- **System Documentation:** Designing the logical flow and performance evaluation metrics.

---

## 📂 Project Structure
- `arduino/`: `.ino` files for the microcontroller logic and sensor calibration.
- `vision_module/`: Python scripts for YOLO detection and video processing.
- `data/`: Sample logs of climatic data and power consumption records.
- `assets/`: Circuit diagrams, detection screenshots, and hardware photos.

## 🚀 Getting Started
1. **Hardware Setup:** Connect your Arduino as per the diagram in `/assets`.
2. **Install Dependencies:** ```bash
   pip install ultralytics pyserial opencv-python
