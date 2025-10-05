def twoSum(arr, target):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                res.append([arr[i],arr[j]])
    return res
    
arr = [1,2,3,46,23,234,6,2,4,2,4,7]
print(twoSum(arr, 8))