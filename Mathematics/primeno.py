# App1
def isPrime(n):
    if n ==1 :
        return False
    i = 2
    while (i*i < n):
        if n%i == 0 :
            return False
        i+=1

    return True

print(isPrime(67))


def isPrime2(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True 

print(isPrime2(67))