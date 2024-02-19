def foo(n):
    if n == 0:
        return 1
    
    else :
        return n*foo(n-1)
    


#print(foo(5))
    
def count_digits(n):
    c = 0 
    while n>0:
        c+=1
        n=n//10

    return print(c)

count_digits(1239023403420)


number = 1239023403420
count = 0

# Loop to count digits
while number != 0:
    number //= 10  # Integer division by 10
    count += 1

print("Number of digits:", count)



print(50*"\()")