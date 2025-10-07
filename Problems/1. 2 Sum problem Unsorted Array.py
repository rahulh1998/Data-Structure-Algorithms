def twosum_unsorted(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            break
        seen[num] = i
    print(len(seen))

numbers = [2, 3, 4, 7, 11, 15] 
target = 9
print(twosum_unsorted(numbers, target))


