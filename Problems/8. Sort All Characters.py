arr = ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]


import random

def sort_array(arr):
    helper(arr, 0, len(arr)-1)
    return arr

def helper(arr, start, end):
    if start >= end:
        return

    # Random pivot
    pi = random.randint(start, end)
    arr[start], arr[pi] = arr[pi], arr[start]
    pivot = arr[start]

    # 3-way partition: < pivot, == pivot, > pivot
    low = start      # arr[start..low-1] < pivot
    mid = start + 1  # arr[low..mid-1] == pivot
    high = end       # arr[high+1..end] > pivot

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:  # arr[mid] == pivot
            mid += 1

    # Recurse on < pivot and > pivot regions
    helper(arr, start, low-1)
    helper(arr, high+1, end)