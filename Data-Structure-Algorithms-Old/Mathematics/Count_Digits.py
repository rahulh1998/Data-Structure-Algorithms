def countDigits(n):
    c = 0
    while n>0:
        c+=1
        n//=10
    return c


print(countDigits(230234043))