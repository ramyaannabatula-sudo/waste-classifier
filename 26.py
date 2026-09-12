def classify_waste(waste):
    if waste == "plastic":
        return "dry waste"
    else:
        return "wet waste"
result = classify_waste("plastic")
print(result)
# plastic goes into the parameter waste
#python checks waste == plastic so return "dry waste"
#"dry waste" get stored in result
#print(result) displays it