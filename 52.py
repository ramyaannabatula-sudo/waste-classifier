'''from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="bus.jpg",
    show=True
)

for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    confidence = float(box.conf[0])

    print(name, round(confidence * 100, 2), "%")

counts = {}
for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
for name, count in counts.items():
    print(name, ":", count)'''
'''from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(source="bus.jpg", show=True)

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
    print(name, ":", count)'''
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(source="bus.jpg", show=True)

counts = {}
confidences = {}

for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    confidence = float(box.conf[0])

    if confidence >= 0.5:
        if name in counts:
            counts[name] += 1
            confidences[name].append(round(confidence * 100, 2))
        else:
            counts[name] = 1
            confidences[name] = [round(confidence * 100, 2)]

for name, count in counts.items():
    print("Object:", name)
    print("Count:", count)
    print("Confidence scores:", confidences[name], "%")
    print()