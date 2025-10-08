import random
"""
Quick Sort Algorithm (Randomized Hoare Partition)

Time Complexity:
    - Best Case:     O(n log n)
    - Average Case:  O(n log n)
    - Worst Case:    O(n^2)   (when pivot choices are consistently poor)

Space Complexity:
    - O(log n) on average (due to recursion stack)
    - O(n) in the worst case (for highly unbalanced partitions)
"""

def qsort(arr, start, end):
    # Base condition
    if start >= end:
        return

    # Pick a random element as pivot
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]

    smaller = start + 1
    bigger = end

    # Partition process
    while smaller <= bigger:
        if arr[smaller] <= arr[start]:
            smaller += 1
        elif arr[bigger] >= arr[start]:
            bigger -= 1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller += 1
            bigger -= 1

    # Place pivot in correct position
    arr[start], arr[bigger] = arr[bigger], arr[start]

    # Recursively sort left and right partitions
    qsort(arr, start, bigger - 1)
    qsort(arr, bigger + 1, end)


def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)
    return arr


# Example usage:
print(quick_sort([5, 3, 8, 4, 2, 7, 1]))
