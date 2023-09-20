# Pattern 18 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for i in range(n):
    for j in range(n-i-1,n):
        print(chr(65+j),end= ' ')
    print()