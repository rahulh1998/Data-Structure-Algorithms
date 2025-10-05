def binarysearch(arr, target, start, end):
    
    # exit if target not in arr
    if start > end:
        return -1

    mid = (start+end)//2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binarysearch(arr, target, start, mid - 1)
    else:
        return binarysearch(arr, target, mid+1, end)

arr = [1,2,3,4,5,6,7,8,9,10]
target = 15
res = binarysearch(arr, target, 0, len(arr)-1)

if res != -1:
    print(f"{target} present at index : {res}")
else:
    print(f"{target} not in {arr}")