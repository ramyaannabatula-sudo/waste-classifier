wet_waste = ['banana','food','apple']
dry_waste = ['glass','paper','plastic']

while True:
    waste = input("Enter the waste(or type stop):").lower()
    if waste == "stop":
        break
    if waste in wet_waste :
        print("wet waste")
    elif waste in dry_waste :
        print("dry waste")
    else:
        print("unknown waste")