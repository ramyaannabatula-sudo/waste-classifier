file = open("waste.csv","r")
next(file)
total_records = 0
wet_count = 0
dry_count = 0
unknown_count = 0
total_weight = 0
for line in file:
    parts = line.strip().split(",")

    total_records += 1

    weight = float(parts[1])
    total_weight += weight

    category = parts[2]
    if category == "wet":
        wet_count += 1
    elif category == "dry":
        dry_count += 1
    else:
        unknown_count += 1
file.close()
waste_types = ['wet', 'dry', 'unknown']
waste_count = [wet_count, dry_count, unknown_count]

for i in range (len(waste_types)):
    print(waste_types[i],":",waste_count[i])
import matplotlib.pyplot as plt

plt.bar(waste_types, waste_count)
plt.xlabel("Waste Type")
plt.ylabel("Number of Wastes")
plt.title("Waste Classification Report")
plt.show()