


myDict = {"name": "Elon Musk", "age": 45, "year": 2021}



def searchDict(dictionary, value):
    for key in dictionary:
        if(dictionary[key] == value):
            return [key, value]
    return []



print(searchDict(myDict, 2021))
