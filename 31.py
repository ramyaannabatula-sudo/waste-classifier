waste_category={'banana': 'wet', 'plastic': 'dry', 'glass': 'dry', 'apple': 'wet', 'paper': 'dry', 'vegetable': 'wet'
,'food':'wet','bottle':'dry'}
while True:
    waste = input("Enter the waste(or type stop):")
    if waste == "stop":
        break
    if waste in waste_category:
        category= waste_category[waste]
        print("category:",category)
    else:
        print("unknown waste")