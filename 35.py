waste_category = {'banana':'wet','plastic':'dry','paper':'dry','food':'wet','glass':'dry'}
def classify_waste(waste):
    if waste in waste_category:
        return waste_category[waste]
    else:
        return "unknown waste"
wet_count = 0
dry_count = 0
unknown_count = 0

wastes = ['banana','plastic','paper','glass','food','lamp']
for waste in wastes:
    category = classify_waste(waste)
    print(waste,'->',category)
    if category == 'wet':
        wet_count += 1
    elif category == 'dry':
        dry_count += 1
    else:
        unknown_count += 1
print("wet count:",wet_count)
print("dry count:",dry_count)
print("unknown_count:",unknown_count)