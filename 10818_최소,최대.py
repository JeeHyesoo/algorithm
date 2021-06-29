import sys

sys.stdin = open("input.txt")

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

array = quick_sort(array)

print(array[0],array[-1])

