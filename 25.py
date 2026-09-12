def identify_waste(waste):
    return "wet waste"
def process_waste(waste):
    category = identify_waste(waste)
    print("category:",category)
process_waste("banana")