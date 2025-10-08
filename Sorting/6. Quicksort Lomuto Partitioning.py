import random

# Quick Sort
# Lomuto's Partitioning InPlace - O(n)
def helperFunction(arr, start, end):
    if start >= end:
        return

    smaller = start
    pivotindex = random.randint(start, end - 1)
    arr[pivotindex], arr[start] = arr[start], arr[pivotindex]
    pivot = arr[start]

    for bigger in range(start + 1, end):
        if arr[bigger] < pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

    arr[smaller], arr[start] = arr[start], arr[smaller]
    return smaller  # partition index

def quicksort(arr, start, end):
    if start >= end:
        return
    
    pivotindex = helperFunction(arr, start, end)
    quicksort(arr, start, pivotindex)
    quicksort(arr, pivotindex + 1, end)
    return arr


arr = [5, 3, 8, 4, 2, 7, 1]
print(quicksort(arr, 0, len(arr)))
