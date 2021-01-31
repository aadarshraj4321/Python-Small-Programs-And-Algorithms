


def pairs(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if(array[i] + array[j] == target):
                #print(i, j)
                return [i, j]
    return []


array = [2, 6, 3, 9, 11]
print(pairs(array, 9))





def findPairs(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if(array[i] + array[j] == target):
                print([i, j])


array = [2, 6, 3, 9, 11, 1]
print(findPairs(array, 12))
