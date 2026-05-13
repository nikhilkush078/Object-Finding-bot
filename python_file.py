import cv2
import serial
import time
from ultralytics import YOLO

# --- CONFIGURATION ---
# If running locally after downloading from Drive:
MODEL_PATH = 'best.pt' 
# Serial port: 'COM3' for Windows, '/dev/ttyUSB0' for Linux/Mac
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

try:
    arduino = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE, timeout=0.1)
    print("Connected to Arduino")
except Exception as e:
    print(f"Error: {e}. Check USB connection.")
    arduino = None

# Load Model
model = YOLO(MODEL_PATH)

# Use IP Webcam address if using phone as camera (e.g., 'http://192.168.1.1:8080/video')
# Or use 0 for built-in webcam
cap = cv2.VideoCapture(0)

# PWM Speed (0-255)
base_speed = 160 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    img_h, img_w, _ = frame.shape
    img_center_x = img_w // 2
    
    # Run YOLO inference
    results = model(frame, conf=0.5)
    annotated_frame = results[0].plot()
    
    detected = False

    for r in results:
        for box in r.boxes:
            detected = True
            # Get center of the bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            obj_center_x = int((x1 + x2) / 2)
            
            # Calculate error from center
            offset = obj_center_x - img_center_x
            
            # Control Logic with PWM
            if offset < -60:    # Object is Left
                cmd = f"L{base_speed}\n"
            elif offset > 60:   # Object is Right
                cmd = f"R{base_speed}\n"
            else:               # Object is Center
                cmd = f"F{base_speed}\n"
            
            if arduino:
                arduino.write(cmd.encode())
            break # Follow the first object found

    if not detected:
        # Rotate Search (RT)
        if arduino:
            arduino.write(f"T{base_speed}\n".encode())

    cv2.imshow("YOLO Car Control", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if arduino:
    arduino.close()
cv2.destroyAllWindows()
