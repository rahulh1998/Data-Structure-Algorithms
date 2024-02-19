def pallindrome(n):#121
    x = n
    res = 0

    while n>0:
        res = res*10 + n%10
        n//=10
    
    if res == x:
        print("Pallindrome")

    else:
        print("Not a pallindrome")


pallindrome(123333353333321)