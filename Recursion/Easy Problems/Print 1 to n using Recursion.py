def print_1_to_n(n):
    # # Approach 1
    # while n>0:
    #     print_1_to_n(n-1)
    #     print(n)
    #     return
    
    # Approach 2
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)
        
print_1_to_n(10)