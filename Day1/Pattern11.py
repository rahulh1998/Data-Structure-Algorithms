# Pattern 11 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5
p = 1
for i in range(1,n+1):
    if i%2 == 0 :
        p=0
    else:
        p=1
    for j in range(i):
        if p == 1:
            print(1,end = ' ')
            p=0
        elif p==0:
            print(0,end = ' ')
            p=1
    print()