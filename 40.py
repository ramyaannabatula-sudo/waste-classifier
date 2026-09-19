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
print("\n------WASTE RECORDS------")
print("total records:",total_records)
print("wet wastes:",wet_count)
print("dry wastes:",dry_count)
print("unknown wastes:",unknown_count)
print("total weight:",total_weight)