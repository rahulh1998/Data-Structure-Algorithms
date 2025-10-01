def bubble_sort(arr):
    for start in range(len(arr)):
        for i in range(len(arr)-1,start,-1):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
    print(arr)
    return arr

bubble_sort([2,4,5,6,6,7,823,23,1,0])
