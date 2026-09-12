wet_waste = ['banana','apple','food','veggies']
dry_waste = ['plastic','paper','glass','bottle']
metal_waste = ['iron','aluminium','steel','can']
waste_record = []
def classify_waste(waste,weight):
    if waste in wet_waste:
        if weight>= 5:
            return "wet waste","compost","Large Amount"
        else:
            return "wet waste","compost","Small Amount"
    elif waste in dry_waste:
        if weight>= 5:
            return "dry waste","recycle","Large Amount"
        else:
            return "dry waste","recycle","Small Amount"
    elif waste in metal_waste:
        if weight>= 5:
            return "metal waste","recycle","Large Amount"
        else:
            return "metal waste","recycle","Small Amount"
    else:
        if weight>= 5:
            return "unknown waste","manual check","Large Amount"
        else:
            return "unknown waste","manual check","Small Amount"


while True:
    waste = input("Enter the waste(or type stop):").lower()
    if waste == 'stop':
        break
    weight = float(input("Enter the weight in kg:"))
    category,method,amount_status = classify_waste(waste,weight)
    waste_record.append((waste,category,weight,amount_status,method))
    print(category,weight,method,amount_status)
print(waste_record)
total_weight = 0

print("\n======WASTE REPORT======")
for waste,category,weight,amount_status,method in waste_record:
    print("waste:",waste)
    print("category:",category)
    print("amount status:",amount_status)
    print("method:",method)
    total_weight = total_weight + weight
print("total weight:",total_weight,"kg")

