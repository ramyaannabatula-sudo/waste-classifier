for i in range(1,6):
    waste = input("enter waste type:")
    if waste == "wet":
        print("wet waste - wet bin")
    elif waste == "dry":
        print("dry waste - dry bin")
    else:
        print("unknown waste type")