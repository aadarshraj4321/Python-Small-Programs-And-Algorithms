



myList = [i for i in range(1, 101)]
newList = myList[:90]
newList.pop()
#print(newList)
newList.append(91)
newList.append(92)
#print(newList)
#print(len(newList))
#print(sum(newList))


def findMissingNum(array, lenArray):
    sum1 = 92 * 93 / 2
    #print(sum1)
    sum2 = sum(array)
    #print(sum2)
    val = sum1 - sum2
    if(sum1 == sum2):
        return True
    else:
        print(val)


findMissingNum(newList, 91)



happily move smoothly without noise or effort like a wind
