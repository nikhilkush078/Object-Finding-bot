from ultralytics import YOLO

model = YOLO('yolov8n.pt')   # or yolov8s.pt, yolov8m.pt etc.

model.train(
    data='/content/drive/MyDrive/object_finding_bot.py/data.yaml',
    epochs=100,
    imgsz=640,
    batch=8,
    project='/content/drive/MyDriveobject_finding_bot.py/runs',
    name='train_data'
)
