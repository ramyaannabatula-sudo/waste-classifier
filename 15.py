waste = []
for i in range(5):
    item = input("enter the waste:").lower()
    waste.append(item)
print(waste)

for item in waste:
    if item == "banana" or item == "fruits":
        print("wet waste")
    elif item == "paper" or item == "plastic" or item == "glass":
        print("dry waste")
    else :
        print("unknown waste")
