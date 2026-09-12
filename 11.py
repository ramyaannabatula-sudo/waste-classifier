wet_waste = ['banana','fruits','food']
dry_waste = ['paper','bottle','plastic','glass']

wet_count = 0
dry_count = 0

for i in range(5):
    print("checking waste",i+1)
    waste = input("enter waste type: ").lower()
    if waste in dry_waste:
        dry_count += 1
        print("dry waste",dry_count)
    elif waste in wet_waste:
        wet_count += 1
        print("wet waste",wet_count)
    else:
        print("unknown waste")
    print("total wet waste",wet_count)
    print("total dry waste",dry_count)

