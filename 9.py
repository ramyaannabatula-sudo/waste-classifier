for i in range(1,6):
    waste = input("enter waste type:")
    if waste == "plastic" or waste == "paper" or waste == "bottle":
       print("dry waste")
    elif waste == "food" or waste == "vegetable" or waste == "fruit":
        print("wet waste")
    else:
        print("unknown waste")
