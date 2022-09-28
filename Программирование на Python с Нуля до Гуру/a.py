age = 22
weight = 58
isMarried = False
result = age > 21 and weight == 58 and isMarried
print(result)  # False, так как isMarried = False

age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True