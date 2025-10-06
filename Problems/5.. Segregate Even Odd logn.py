# Segragate even odd
def segregate_even_odd(arr):
    i = 0
    j = len(arr)-1

    while i<j:
        if arr[i]%2 == 0 and arr[j]%2 == 0:
            i+=1
        elif arr[i]%2==0 and arr[j]%2!=0:
            i+=1
            j-=1
        elif arr[i]%2!=0 and arr[j]%2==0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        else:
            j-=1

    return arr


arr = [1,2,3,9,2,4,5,7,9,1,2,3,4,5,7,9,4] # [2,4, 1,3]
print(segregate_even_odd(arr))