# 💡 AI-Driven Smart Street Lighting System
### Edge AI Implementation using Raspberry Pi 4B, Object Detection, and Climatic Data

[![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%204B-C51A4A.svg)](https://www.raspberrypi.com/)
[![AI](https://img.shields.io/badge/AI-YOLOv8-red.svg)](#)
[![Protocol](https://img.shields.io/badge/Protocol-MQTT%2FHTTP-blue.svg)](#)

## 📌 Project Overview
This system addresses urban energy inefficiency by introducing a **Context-Aware Lighting System**. By deploying **Edge AI** on a Raspberry Pi 4B, the project utilizes real-time **Object Detection** (YOLO) and **Sensor Fusion** (LDR & Climatic data) to control street lighting dynamically.

The system transitions from low-power idle modes to full luminosity only when road users are detected or when adverse weather conditions (fog/rain) necessitate increased visibility.

---

## ⚙️ System Architecture
The project operates through a multi-layered communication and decision pipeline:
1. **Vision Layer:** Raspberry Pi Camera captures real-time video; YOLO model performs inference at the edge.
2. **Communication Layer:** Detection results are transmitted via **MQTT/HTTP** protocols to a NodeMCU (ESP8266) node.
3. **Climatic Layer:** NodeMCU integrates real-time data from **LDR** and **DHT11** sensors.
4. **Control Logic:** A decision matrix adjusts PWM signals/Relays to dim or brighten lights based on the combined vision and environmental inputs.



---

## 🛠️ Technologies & Hardware
**Compute & Control:**
- **Raspberry Pi 4B:** Local AI inference and master controller.
- **NodeMCU (ESP8266):** Wireless actuator and sensor gateway.
- **Sensors:** Camera Module, LDR (Lux levels), DHT11 (Climatic data).

**Software Stack:**
- **AI/CV:** Python, OpenCV, YOLO (Ultralytics).
- **Communication:** MQTT Protocol, PySerial.
- **Firmware:** C++ (Arduino IDE) for NodeMCU logic.

---

## 👥 Group Project & Collaboration
This project was developed as a collaborative major project by a team of four. My primary technical contributions included:
- **Edge AI Deployment:** Optimizing the YOLO architecture for the Raspberry Pi 4B environment.
- **Communication Pipeline:** Developing the MQTT/HTTP bridge between the Pi and the NodeMCU actuator.
- **System Logic:** Designing the decision-making algorithms that balance energy saving with safety requirements.

---

## 📂 Project Structure
- `models/`: Trained YOLO weight files and configuration.
- `scripts/`: Python source code for detection and communication.
- `hardware/`: Circuit diagrams and pinout configurations.
- `requirements.txt`: Environment dependencies.

## 🚀 Setup & Execution
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/smart-ai-street-light.git](https://github.com/your-username/smart-ai-street-light.git)
