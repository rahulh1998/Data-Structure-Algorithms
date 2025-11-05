# Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number. 

# Examples : 

# Input: d = 7                                                         
# Output: 111
# Explanation:  2^0 + 2^1  + 2^2 = 1+2+4 = 7.

# Input: d = 10
# Output: 1010
# Explanation: 2^1  + 2^3 = 2+8 = 10.



# Decimal to binary conversion
# using recursion

def decimal_to_binary(n):
    if n==0:
        return 0

    return (n%2 + 10*decimal_to_binary(n//2))

print(decimal_to_binary(7))
