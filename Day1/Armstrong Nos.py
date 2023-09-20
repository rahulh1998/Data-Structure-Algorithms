n= 153
num = n
sum = 0 
while n!= 0 :
    r = n%10
    sum = sum + r*r*r
    n = n//10

if num == sum:
    print('Armstrong No !!')
else:
    print("Not an Armstrong No...")

print(sum)