def check_waste(waste):
    print("checking waste:",waste)
    if waste== "banana":
        return "wet waste"
    else :
        return "dry waste"
result = check_waste("banana")
print(result)