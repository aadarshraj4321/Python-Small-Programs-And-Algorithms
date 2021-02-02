

myDict = {"name": "Elon Musk", "age": 45, "year": 2021, "company": "SpaceX"}
print(f"This is main dict : {myDict}")
print()

print("===================copy()===================")
newDict = myDict.copy()
print(f"This is new dict: {newDict}")
print()
print()

print("===================fromkeys()===================")
dictFromKeys ={}.fromkeys([1, 2, 3], 0)
print(dictFromKeys)
print()

print("===================get()===================")
print(myDict.get("AnotherCompany", "Tesla"))
print(myDict)
print()

print("===================items()===================")
print(myDict.items())
print()


print("===================keys()===================")
print(myDict.keys())
print()

print("===================popitem()===================")
print(myDict.popitem())
print(myDict)
print()

print("===================setdeafault()===================")
print(myDict.setdefault("company1", "Tesla"))
print(myDict)
print()

print("===================pop()===================")
print(myDict.pop("age"))
print()


print("===================values()===================")
print(myDict.values())
print()


print("===================update()===================")
print(myDict)
newDict ={"Born": "South Africa", "Living": "USA"}
myDict.update(newDict)
print(myDict)
print()

print("===================clear()===================")
myDict.clear()
print(myDict)
























