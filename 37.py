waste_record = []
waste_category = {'banana':'wet','plastic':'dry','paper':'dry','apple':'wet','glass':'dry','food':'wet'}
def classify_waste(waste, weight):
    if waste in waste_category:
        category = waste_category[waste]
    else:
        category = "unknown waste"
    if weight >= 5:
        amount_status = "large amount"
    else:
        amount_status = "small amount"
    return category, amount_status


while True:

    waste = input("Enter your waste(or type stop): ")

    if waste == "stop":
        break
    while True:

        try:
            weight = float(input("Enter weight in kg: "))
            break
        except:
            print("Invalid weight , try again")
    category, amount_status = classify_waste(waste, weight)
    record = {
        "category":category,
        "amount_status":amount_status,
        "waste":waste,
        "weight":weight
    }
    waste_record.append(record)
for record in waste_record:
    print("Waste:", record["waste"])
    print("Weight:", record["weight"], "kg")
    print("Category:", record["category"])
    print("Amount:", record["amount_status"])
    print()
    
