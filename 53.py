'''from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(source="water-bottles-many-white-background-30910433.jpg", show=True)

bottle_count = 0

for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    confidence = float(box.conf[0])
    print(name, round(confidence * 100, 2), "%")
    if name == "bottle" and confidence >= 0.5:
        bottle_count += 1

print("Bottles detected:", bottle_count)'''
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="ChatGPT Image Oct 14, 2026, 11_23_27 AM.png",show=True
)

counts = {}

for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    confidence = float(box.conf[0])

    if confidence >= 0.5:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

for name, count in counts.items():
    print(name, ":", count)