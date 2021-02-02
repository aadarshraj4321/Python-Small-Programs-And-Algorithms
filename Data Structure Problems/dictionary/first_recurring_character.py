

# Time Comp = O(N) | Space Comp = O(N)
def firstRecurring(array):
    newDict = {}
    for i in array:
        if(i in newDict):
            return i
        else:
            newDict[i] = True
    return []


array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array))


array1 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array1))


array2 = [2, 3, 4, 5]
print(firstRecurring(array2))

array2 = []
print(firstRecurring(array2))

print()
print()








# Time Comp = O(N^2) | Space Comp = O(1)
def firstRecurring(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if(array[i] == array[j]):
                return array[i]
            else:
                i += 1

    return []


array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array))


array1 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array1))


array2 = [2, 3, 4, 5]
print(firstRecurring(array2))

array2 = []
print(firstRecurring(array2))

print()
print()












# Time Comp = O(N) | Space Comp = O(N)
def firstRecurring(array):
    table = {}
    for i in range(len(array)):
        if(array[i] in table):
            return array[i]
        else:
            table[array[i]] = i
    return []





array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array))


array1 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
print(firstRecurring(array1))


array2 = [2, 3, 4, 5]
print(firstRecurring(array2))

array2 = []
print(firstRecurring(array2))


















