waste_category = {'banana':'wet','plastic':'dry','apple':'wet','paper':'dry','food':'wet','veggies':'wet','glass':'dry','bottle':'dry'}
wet_count = 0
dry_count = 0
unknown_count = 0


def classify_waste(waste):
    if waste in waste_category:
        category = waste_category[waste]
        return category
    else:
        return "unknown"
while True:
    waste = input("Enter the waste(or type stop):")
    if waste=="stop":
        break
    category = classify_waste(waste)
    print("category:",category)
    if category == "wet":
        wet_count += 1
    elif category == "dry":
        dry_count += 1
    else:
        unknown_count += 1

print("wet count:",wet_count)
print("dry count:",dry_count)
print("unknown_count:",unknown_count)



