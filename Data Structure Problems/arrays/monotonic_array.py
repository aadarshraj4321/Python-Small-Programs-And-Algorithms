import string

def monotonicArray(array):
    if(len(array) <= 2):
        return True
    isIncrease = True
    isDecrease = True
    p0 = 1
    p1 = 0
    for i in range(1, len(array)):

        if(array[p0] < array[p1]):
            isIncrease = False
        elif(array[p0] > array[p1]):
            isDecrease = False
        p0 += 1
        p1 += 1

    return (isIncrease or isDecrease)


array = [1,2,2,3]
print(monotonicArray(array))


array = [2, 1, 0, -1, 3]
print(monotonicArray(array))
