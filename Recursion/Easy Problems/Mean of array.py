# https://www.geeksforgeeks.org/dsa/mean-of-array-using-recursion/

# Given an array of numbers, you are required to calculate the mean (average) using recursion.

# Note: The mean of an array is the sum of its elements divided by the number of elements in the array.

# Examples: 

# Input: 1 2 3 4 5
# Output: 3
# Explanation: The sum of elements (15) divided by the number of elements (5) gives the mean: 3

# Input: 1 2 3
# Output: 2
# Explanation: The sum of elements (6) divided by the number of elements (3) gives the mean: 2


def helper(nums,i):
    if i<0:
        return 0
    
    sum = helper(nums,i-1)
    print("returning, ", nums[i-1] )
    return  nums[i-1]

def mean_of_array(nums):
    len_arr = len(nums)-1

    print(helper(nums, len_arr))

nums = [1, 2, 3, 4, 5]    # [i for i in range(1,6)]
mean_of_array(nums)