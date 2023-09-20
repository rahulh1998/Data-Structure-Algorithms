# Pattern 10 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for i in range(n):
    print((i+1)*'* ')
    if i==n-1:
        for j in range(n):
            print((n-j-1)*'* ')
