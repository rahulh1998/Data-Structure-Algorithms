# Pattern 9 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for i in range(n):
    print((n-i-1)*' '+(2*i+1)*'*')
for i in range(n):
    print((i)*' '+(2*(n-i-1)+1)*'*')