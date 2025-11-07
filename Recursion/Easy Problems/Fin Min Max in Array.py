def find_min_max(arr):
    result = helper(arr, len(arr)-1)
    return result

def helper(arr, index):
    if index == 0:
        return [arr[0],arr[1]]

    result = helper(arr,index-1)

    if arr[index] < result[0]:
        result[0] = arr[index]
    elif arr[index] > result[1]:
        result[1] = arr[index]
    return result

print(find_min_max([1,2,3,19,4,5,-1]))

