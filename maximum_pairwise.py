
def maxi(arr):
    arr_sorted = sorted(arr)
    final_sub = arr_sorted[-1] * arr_sorted[-2]
    return final_sub
        


input_n = int(input())

input_numbers = [int(x) for x in input().split()]
print(maxi(input_numbers))
