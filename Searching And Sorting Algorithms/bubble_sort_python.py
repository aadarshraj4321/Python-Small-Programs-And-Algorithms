## Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
            


arr = [4,45,3,6,2,651,1,8]
bubble_sort(arr)

