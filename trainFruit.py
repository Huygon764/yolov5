from ultralytics import YOLO

# Load the YOLOv5 model
model = YOLO("yolov5su.pt")  # Pre-trained small model as base

# Train the model
model.train(data="./dataset/dataset.yaml", epochs=50, imgsz=640, batch=16, project="fruit_detects")
