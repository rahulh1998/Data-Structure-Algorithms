def allDivisors1(n):
    for i in range(1,(n//2)+1):
        if n%i == 0:
            print(i)
    print(n)

allDivisors1(7)


def allDivisors(n):
    i=1
    while i*i <= n:
        if n%i == 0:
            print(i)
        i+=1

allDivisors(100)