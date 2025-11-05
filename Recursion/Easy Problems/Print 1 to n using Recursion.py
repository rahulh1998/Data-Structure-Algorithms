def print_1_to_n(n):
    while n>0:
        print_1_to_n(n-1)
        print(n)
        return

print_1_to_n(10)