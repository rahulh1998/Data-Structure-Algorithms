def selectionsort(A):
    for i in range(len(A)): # Iterating over each element
        minvalue = A[i] 
        minindex = i
        for green in range(i+1, len(A)):
            if A[green] < minvalue:
                minvalue = A[green]
                minindex = green
        A[i], A[minindex] = A[minindex],A[i]

    print(A)


selectionsort([64, 25, 12, 22, 11])