def sum_n_naturals(n):
    if n==0:
        return 0 
    return n + sum_n_naturals(n-1)

print(sum_n_naturals(5))
