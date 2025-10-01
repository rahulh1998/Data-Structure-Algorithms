def InsertionSort(A):

    for i in range(len(A)):
        temp = A[i] # get current element
        red = i-1

        while red>=0 and A[red] > temp: # if previous element is greater than current element then shift right 
            A[red+1] = A[red]
            red-=1
        
        A[red+1] = temp # assign element in correct position

    print(A)
    return A

InsertionSort([1,3,56,2,1,4,7,23,6,23,12,12])