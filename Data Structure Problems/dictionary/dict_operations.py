
myDict = {"name": "Elon Musk", "age": 45, "year": 2021, "company": "SpaceX"}

print(45 in myDict)

print(45 in myDict.values())



for key in myDict:
    print(key, myDict[key])

print()

newDict = {0: False, 1: False, 2:False}
print(all(newDict))
newDict = {}
print(any(newDict))
print(len(myDict))
print(sorted(myDict, reverse=True))
