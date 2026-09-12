wet_waste_types = ['banana','food','apple']
dry_waste_types = ['paper','plastic','glass']


wet_waste = []
dry_waste = []
unknown_waste = []

while True:
    waste = input("Enter the waste(or type stop):").lower()
    if waste == "stop":
        break
    if waste in wet_waste_types:
        wet_waste.append(waste)
    elif waste in dry_waste_types:
        dry_waste.append(waste)
    else :
        unknown_waste.append(waste)


print("\n------WASTE REPORT-------")
print("wet_waste",wet_waste)
print("total wet_waste:",len(wet_waste))
print("dry_waste",dry_waste)
print("total dry_waste:",len(dry_waste))
print("unknown_waste",unknown_waste)
print("total unknown_waste:",len(unknown_waste))