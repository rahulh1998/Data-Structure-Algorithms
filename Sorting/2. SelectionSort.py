def SelectionSort(a):
    for i in range(len(a)):
        minindex = i
        for green in range(i+1, len(a)):
            if a[green] < a[minindex]:
                minindex = green
        a[i],a[minindex] = a[minindex], a[i]

    print(a)

SelectionSort([1,324,4365,3455346,23,2,123,546])