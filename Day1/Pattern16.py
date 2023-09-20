# Pattern 16 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end = ' ')
    print()
