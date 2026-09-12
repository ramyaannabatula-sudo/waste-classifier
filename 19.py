waste = ["banana","food","veggies","plastic","paper","glass"]

for i in range(8):
    waste = input("Enter the waste:").lower()
    if waste == "banana" or waste == "food" or waste == "veggies":
        print("wet waste",waste)
    elif waste == "plastic" or waste == "paper" or waste == "glass":
        print("dry waste",waste)
    else :
        print("unknown waste",waste)