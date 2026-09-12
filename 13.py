# def = function
# check_waste = name of the function
# waste = transport medium
def check_waste(waste):
    if waste == "food":
        print("wet waste")
    elif waste == "paper":
        print("dry waste")

# return = give this result back to me

def add(a,b):
    return a+b
result = add(2,3)
print(result)


def check_waste(waste):
    if waste == "food":
        return "wet waste"
    elif waste == "paper":
        return "dry waste"
result = check_waste("food")
print(result)


