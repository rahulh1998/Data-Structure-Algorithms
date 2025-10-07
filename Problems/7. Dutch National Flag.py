# Dutch National Flag
# Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

# Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.

# This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).

# Example
# {
# "balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
# }
# Output:

# ["R", "R", "G", "G", "G", "G", "B", "B"]
# There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.

# Notes
# Constraints:

# 1 <= n <= 100000
# Do this in ONE pass over the array, NOT TWO passes
# Solution is only allowed to use constant extra memory


# Dutch National Flag - Main idea is to sort only red and blue rest will automatically get sorted
def dutch_flag(balls):
    i = 0
    rp = 0
    bp = len(balls) - 1

    while i <= bp:

        if balls[i] == 'R': # If red found 
            balls[i],balls[rp] = balls[rp],balls[i]
            # print(f'{i}. Red at {i} swapped to {rp} : {balls}. RP = {rp+1}')
            rp+=1
            i+=1

        elif balls[i] == 'B':
            balls[i],balls[bp] = balls[bp],balls[i]
            # print(f'{i}. Blue at {i} swapped to {bp} : {balls}. BP = {bp+1}')
            bp-=1

        else:
            # print(i)
            i+=1

    return balls

print(dutch_flag(balls = ['G','B','G','G','R','B','R','G']  ))