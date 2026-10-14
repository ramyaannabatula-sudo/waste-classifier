'''from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in an image
results = model.predict(source="134256573812053395.jpg", show=True)

print(results[0].boxes)'''
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    show=True,
    save=True
)

print(results[0].boxes)