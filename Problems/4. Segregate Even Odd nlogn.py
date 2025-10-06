def helper(numbers, start , end):
    if start == end:
        return numbers
    mid = (start+end)//2
    helper(numbers, start, mid)
    helper(numbers, mid+1, end)
    
    i = start
    j = mid+1
    aux = []
    
    while i<=mid:
        if numbers[i]%2==0:
            aux.append(numbers[i])
            i+=1
        
    while j<=end:
        if numbers[j]%2==0:
            aux.append(numbers[j])
            j+=1
    
    i = start
    while i<=mid:
        if numbers[i]%2!=0:
            aux.append(numbers[i])
            i+=1
    
    j = mid+1
    while j<=end:
        if numbers[j]%2!=0:
            aux.append(numbers[j])
            j+=1
        
    numbers[start:end+1] = aux
    
    return numbers
        


def segregate_evens_and_odds(numbers):
    start = 0
    end = len(numbers)-1
    numbers = helper(numbers, start, end)
    return numbers