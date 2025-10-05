def binarysearch(arr, target, start, end):

    while start <= end:

        mid = (start + end )//2

        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1
    
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
res = binarysearch(arr, target, 0, len(arr)-1)

if res != -1:
    print(f"{target} present at index : {res}")
else:
    print(f"{target} not in {arr}")