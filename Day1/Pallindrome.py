n = 11001454541
org = n
num = 0
while n!=0:
    r = n%10
    num = num*10 + r
    n = n//10

if org == num:
    print("Pallindrome")
else:
    print("Not a pallindrome.....")