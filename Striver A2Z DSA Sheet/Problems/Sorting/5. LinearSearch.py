def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1



print(search([11,1,1,1,1,1,1],111))