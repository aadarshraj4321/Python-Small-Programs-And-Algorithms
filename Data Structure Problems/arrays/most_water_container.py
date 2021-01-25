

def mostWater(array):
    max_score = 0
    for i in range(len(array)):
        #cu_num = i
        for j in range(i + 1, len(array)):
            #p_num = j
            height = min(array[i], array[j])
            width = j - i
            area = height * width
            max_score = max(max_score, area)
            #if(max_score < area):
                #max_score = area
    return max_score



array = [7, 1, 2, 3, 9]
print(mostWater(array))

array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(mostWater(array))





water = [3,  0,  0,  2,  0,  4]
print(mostWater(water))















def mostWater(array):
    max_score = 0
    p1 = 0
    p2 = len(array)-1
    while(p1 < p2):
        for i in range(len(array)):
            area = min(array[p1], array[p2]) * (p2 -p1)
            max_score = max(max_score, area)
            if(array[p1] < array[p2]):
                p1 += 1
            else:
                p2 -= 1
    return max_score




array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(mostWater(array))


array = [7, 1, 2, 3, 9]
print(mostWater(array))


array = [1,8,100,2,100,4,8,3,7]
print(mostWater(array))


water = [3,  0,  0,  2,  0,  4]
print(mostWater(water))





