def factorial(n): #
    fact = 1
    while n>0:
        fact = fact*(n)
        n-=1
    print(f"Factorial of {n} is {fact}")

factorial(5)
