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
    if waste == "":
        print("Please enter a waste name.")
        continue
    while True:

        try:
            weight = float(input("Enter weight in kg: "))
            break
        except:
            print("Invalid weight , try again")
    category, amount_status = classify_waste(waste, weight)
    file = open("waste.csv","a")
    file.write(waste+"," + str(weight)+"," + category +"," + amount_status + "\n" )
    file.close()
file = open("waste.csv", "r")

for line in file:
    print(line.strip())

file.close()