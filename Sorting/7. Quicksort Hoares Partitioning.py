import random

def qsort(arr, start, end):
    if start >= end:
        return
    # Pick a random element as pivot.
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]
    
    smaller = start + 1
    bigger = end
    
    while smaller <= bigger:
        if arr[smaller] <= arr[start]:
            smaller+=1
        elif arr[bigger] >= arr[start]:
            bigger-=1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller -= 1
            bigger += 1
    
    arr[start], arr[bigger] = arr[bigger], arr[start]
    qsort(arr, start, smaller - 1)
    qsort(arr, smaller + 1, end)

def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)
    return arr


print(quick_sort([5, 3, 8, 4, 2, 7, 1]))