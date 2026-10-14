from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="ChatGPT Image Oct 14, 2026, 11_23_27 AM.png",
    show=True
)

all_counts = {}
accepted_counts = {}

for box in results[0].boxes:
    class_id = int(box.cls[0])
    name = model.names[class_id]
    confidence = float(box.conf[0])

    # Count every detection
    if name in all_counts:
        all_counts[name] += 1
    else:
        all_counts[name] = 1

    # Count detections with confidence >= 50%
    if confidence >= 0.5:
        if name in accepted_counts:
            accepted_counts[name] += 1
        else:
            accepted_counts[name] = 1

print("\n--- All YOLO Detections ---")
for name, count in all_counts.items():
    print(name, ":", count)

print("\n--- Detections Accepted (50% or higher) ---")
for name, count in accepted_counts.items():
    print(name, ":", count)