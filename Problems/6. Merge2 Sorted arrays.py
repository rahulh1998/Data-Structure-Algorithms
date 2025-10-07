# Merge One Sorted Array Into Another
# First array has n positive numbers, and they are sorted in the non-descending order.

# Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.

# Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

# Example
# {
# "first": [1, 3, 5],
# "second": [2, 4, 6, 0, 0, 0]
# }
# Output:

# [1, 2, 3, 4, 5, 6]
# Notes
# Constraints:

# 1 <= n <= 105
# 1 <= array elements (except those zeroes) <= 2 * 109
# You can use only constant auxiliary space.

def merge_sorted(first, second):
    i = 0
    j = 0

    while j<len(second) and i < len(first):

        if  first[i] < second[j]:
            first[i], second[j] = second[j], first[i]
            j+=1

        elif (first[i] > second[j]) and second[j] == 0:
            first[i], second[j] = second[j], first[i]
            i+=1
            j=0

        else:
            j+=1

    return second

print(merge_sorted([1,3,5], [2,4,6,0,0,0]))    
