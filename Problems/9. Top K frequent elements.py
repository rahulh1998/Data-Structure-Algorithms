d = {}
l = []

arr = [1, 2, 3, 2, 4, 3, 1]

for i in arr:
    if i not in arr:
        d[i] = 0
    else:
        d[i]+=1

for i in d.items():
    print(i)