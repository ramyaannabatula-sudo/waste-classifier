def classify_waste(waste):
    if waste == "banana" or waste == "food" or waste == "apple":
        return "Wet Waste"
    else :
        return "Dry Waste"


print(classify_waste("banana"))
print(classify_waste("plastic"))
print(classify_waste("apple"))

# waste = parameter
# banana = argument

