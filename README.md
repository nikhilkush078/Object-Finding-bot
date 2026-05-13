# 🏎️ YOLOv8 Autonomous Object-Following Car

![YOLOv8](https://img.shields.io/badge/YOLOv8-Real--time%20Detection-blueviolet)
![Arduino](https://img.shields.io/badge/Arduino-Hardware%20Control-00979D)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An advanced robotics project that bridges **Computer Vision** and **Embedded Systems**. This car uses a custom-trained YOLOv8 model to detect specific objects via a mobile camera and autonomously navigates toward them using an Arduino-based motor system.[cite: 1, 2]

---

## 📺 Video Demonstration
Check out the car in action! Click the link below to view the demonstration:

👉 **[Watch the Project Demo on LinkedIn](https://www.linkedin.com/posts/nikhil-kushwah-664304218_object-detection-bot-ugcPost-7401494557437272065-dnbK?utm_source=share&utm_medium=member_desktop&rcm=ACoAADbcwqwBmaWPICVZ41SWioXWKvjFBQHsI24)** *(Note: Replace this with your actual LinkedIn post URL)*[cite: 2]

---

## 🚀 Key Features
*   **Real-time Object Tracking:** Uses Ultralytics YOLOv8 for high-speed detection and bounding box calculation.[cite: 2]
*   **Dynamic Speed Control:** Implemented PWM (Pulse Width Modulation) to adjust motor speed directly from the Python script.[cite: 1, 2]
*   **Auto-Search Mode:** The car rotates on its axis (`T` signal) when no object is in sight until it re-acquires its target.[cite: 1, 2]
*   **Proportional Steering:** Automatically turns left, right, or moves straight based on the object's pixel coordinates.[cite: 1, 2]

---

## ⚙️ How It Works

### 1. The Detection (Python Brain)
The Python script captures the video stream and calculates the **Error Offset**:
*   **Center of Frame ($C$):** Image Width / 2[cite: 1]
*   **Target Center ($O_x$):** $(x_1 + x_2) / 2$[cite: 1]
*   **Logic:** The script calculates $Error = O_x - C$.[cite: 1]
    *   If `Error < -60` → Send `L` (Left).[cite: 1]
    *   If `Error > 60` → Send `R` (Right).[cite: 1]
    *   Otherwise → Send `F` (Forward).[cite: 1]

### 2. The Communication
Python sends formatted strings over Serial to the Arduino:
*   `F150\n` -> Move **Forward** at **150** PWM speed.[cite: 1, 2]
*   `L180\n` -> Turn **Left** at **180** PWM speed.[cite: 2]
*   `T140\n` -> **Search** (Rotate) at **140** PWM speed.[cite: 2]

### 3. The Execution (Arduino Muscles)
The Arduino receives the character and the integer, then drives the motors using `analogWrite()` for speed and `digitalWrite()` for direction via an H-Bridge driver.[cite: 1, 2]

---

## 🛠️ Hardware Requirements
*   **Microcontroller:** Arduino Uno / Nano[cite: 2]
*   **Motor Driver:** L298N H-Bridge[cite: 2]
*   **Chassis:** 4WD or 2WD Robot Car Kit[cite: 2]
*   **Camera:** Mobile Phone (using IP Webcam app) mounted on the front[cite: 2]
*   **Power:** 7.4V - 11.1V battery (External power for motors is critical)[cite: 1, 2]

---

## 📂 Project Structure
```bash
# Full Directory Path for Google Drive & Colab
/content/drive/MyDrive/test/
├── runs/
│   └── train_data/
│       └── weights/
│           └── best.pt          # The real location of your trained model
├── yolo_tracker.py              # Python script for AI & Serial communication[cite: 1]
├── car_control/
│   └── car_control.ino          # Arduino sketch for motor logic[cite: 1]
├── test_img.jpg                 # Sample image used for testing[cite: 1]
└── README.md                    # Project documentation
