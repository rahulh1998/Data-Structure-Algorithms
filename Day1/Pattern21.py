# Pattern 21 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 6

for j in range(n):
    if j == 0 or j == n-1:
        print(n*'*')
    else:
        print("*"+(n-2)*' '+'*')
