# Pattern 20 : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = 5

for j in range(n):
    print((j+1)*'*' + (n-j-1)*2*' ' +  (j+1)*'*')
    if j == n-1:
        for i in range(n):
            print((n-i)*'*' + (i*2)*' '+(n-i)*'*')