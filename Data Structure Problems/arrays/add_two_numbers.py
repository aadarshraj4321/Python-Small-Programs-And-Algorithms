

def twoSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while(left < right):
        cu_num = array[left] + array[right]
        if(cu_num == target):
            return [left, right]
        elif(cu_num < target):
            left += 1
        elif(cu_num > target):
            right -= 1
    return []
    
        
array = [3, 2, 3]
print(twoSum(array, 6))
























        
array = [3, 2, 3]
print(twoSum(array, 6))


