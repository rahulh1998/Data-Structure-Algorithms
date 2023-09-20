# Pattern 17 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for i in range(1,n+1):
    print((n-i)*' ',end='')

    for j in range(1,i+1):
        print(chr(64+j),end='')
        
    for k in range(i,1,-1):
        print(chr(64+k-1),end='')

    print()

