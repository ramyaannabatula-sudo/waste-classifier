Waste = ["plastic","vegetable","glass","food","banana"]
wet_waste = []
dry_waste = []
for i in range(5):


    item = input("Enter the item: ")


    if item == "banana" or item == "vegetable" or item == "food":

        wet_waste.append(item)
    else :
        dry_waste.append(item)
print("wet_waste:", wet_waste)
print("Number of wet_waste:", len(wet_waste))
print("dry_waste:", dry_waste)
print("Number of dry_waste:", len(dry_waste))
