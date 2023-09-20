# Pattern 12 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 4

for i in range(1,n+1):
    for j in range(i):
        print(j+1,end='')

    print(((n-i)*2)*' ',end='')

    for l in range(i,0,-1):
        print(l,end= '')
    print()