wet_waste = ['banana','food','apple']
dry_waste = ['glass','paper','plastic']


for i in range(7):
    waste = input("Enter the waste:").lower()
    if waste in wet_waste:
        print("wet waste",waste)
    elif waste in dry_waste:
        print("dry waste",waste)
    else:
        print("unknown waste",waste)