


myDict = {"name": "Elon Musk", "age": 45, "year": 2021}
print(myDict)


myDict.pop("age")
print(myDict)


myDict.popitem()
print(myDict)

myDict.clear()
print(myDict)
print()

del myDict

# Now myDict is not defined because del is deleted the myDict
print(myDict)
