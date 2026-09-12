wet_waste = ['banana','fruits','food']
dry_waste = ['paper','bottle','plastic','glass']
for i in range(1,10):
    waste = input("enter waste type: ").lower()
    if waste in wet_waste:
        print("wet waste")
    elif waste in dry_waste:
        print("dry waste")
    else :
        print("unknown waste")