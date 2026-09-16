waste_category = {'banana':'wet','plastic':'dry','paper':'dry','apple':'wet','glass':'dry'}
def classify_waste(waste,weight):
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
    waste = input("Enter waste (or type stop): ")

    if waste == "stop":
        break


    while True:

        try:
            weight = float(input("Enter weight in kg: "))
            print("Weight:", weight)
            break
        except:
            print("Invalid weight , try again")
    category, amount_status = classify_waste(waste, weight)
    print("category:", category)
    print("amount_status:", amount_status)