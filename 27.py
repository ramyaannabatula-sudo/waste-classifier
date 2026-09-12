#returning more than one value
def waste_info(waste):
    if waste=="banana":
        return "wet waste","compost"
    else:
        return "dry waste","recycle"
category,method = waste_info("banana")
print(category)
print(method)