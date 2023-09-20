n = 18
c = 0

for i in range(2,n+1):
    if n%i==0:
        c+=1

if c is 1:
    print(f"It is a prime  : {n}")
else:
    print(f'{n} is Not a prime no')