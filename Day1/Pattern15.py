# Pattern 15 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end = ' ')
    print()
