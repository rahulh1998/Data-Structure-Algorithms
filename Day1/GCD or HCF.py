n1 = 4
n2 = 6

for i in range(1,min(n1,n2)):
    if n1%i == 0 and n2%i == 0:
        ans  = i

print(ans)