# Pattern 6 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end= ' ')
    print()