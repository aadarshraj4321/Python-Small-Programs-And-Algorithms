def biggest_num(arr):
    big_num = 0
    for i in arr:
        if i>big_num:
            big_num = i
    return big_num



arr = [10,20,30,40,50,100,120,20,30]

print(biggest_num(arr))
