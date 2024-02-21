
def gcd(a,b):
    while a!=b:
        if a >b:
            a = a-b
    
        else:
            b = b-a 
    return a

def gcd2(a,b):
    if b==0:
        return a
    return gcd(b,a%b)



print(gcd(2,15))

print(gcd2(12,15))

