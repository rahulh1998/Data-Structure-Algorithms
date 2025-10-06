def twosum_unsorted(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            print(seen[complement], i)
            break
        seen[num] = i


numbers = [2, 3, 4, 7, 11, 15]  # must be sorted
target = 9
print(twosum_unsorted(numbers, target))
