n = 1023243242344324234

# Sol 1 - Simplest
print('No of digits in n is ',len(str(n)))

# Sol 2

c=0
while n!=0:
    n = n//10
    c+=1

print(c)
