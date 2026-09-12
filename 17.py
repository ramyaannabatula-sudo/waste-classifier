Waste = ["plastic","vegetable","glass","food","banana"]
wet_waste = []
dry_waste = []

for item in Waste:
    if item == "food" or item == "vegetable" or item == "banana":
        wet_waste.append(item)
    else :
        dry_waste.append(item)

print("wet_waste:", wet_waste)
print("dry_waste:", dry_waste)

print("Number of wet waste is: ", len(wet_waste))
print("Number of dry waste is: ", len(dry_waste))

item : input("Enter the waste:")
print(item)

