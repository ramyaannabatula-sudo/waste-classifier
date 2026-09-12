wastes = ["apple","paper","plastic","food","glass","vegetable","banana","leaves"]
for waste in wastes:
    wet_waste = ["apple","food","vegetable","banana","leaves"]
    dry_waste = ["paper","plastic","glass"]
    if waste in wet_waste:
        print("wet waste")
    else :
        print("dry waste")
