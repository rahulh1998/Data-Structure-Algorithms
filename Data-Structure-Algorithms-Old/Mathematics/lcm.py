def lcm(a,b):
    res = max(a,b)
    while True:
        if res%a == 0 and res%b==0:

            return res
        res+=1


def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def lcm2(a,b):
    return a*b//gcd(a,b)

print(lcm(12,15))

print(lcm2(12,15))