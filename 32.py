waste_category={'banana': 'wet', 'plastic': 'dry', 'glass': 'dry', 'apple': 'wet', 'paper': 'dry', 'vegetable': 'wet'
,'food':'wet','bottle':'dry'}
wet_count=0
dry_count=0
unknown_waste_count=0

while True:
    waste = input("Enter the waste(or type stop:")
    if waste == "stop":
        break
    if waste in waste_category:
        category = waste_category[waste]
        print("category:",category)
        if category == "wet":
            wet_count += 1
        else:
            dry_count += 1
    else:
        print("unknown waste")
        unknown_waste_count += 1


print("\n=======WASTE REPORT=======")
print("wet:",wet_count)
print("dry:",dry_count)
print("unknown waste:",unknown_waste_count)
