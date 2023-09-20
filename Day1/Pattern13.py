# Pattern 13 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5
no = 1
for i in range(1,n+1):
    for j in range(i):
        print(no,end= ' ')
        no+=1
    print()