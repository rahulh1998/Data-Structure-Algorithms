# Second Largest Element

# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


# Examples:
# Input: nums = [8, 8, 7, 6, 5]

# Output: 7

# Explanation:

# The largest value in nums is 8, the second largest is 7

# Input: nums = [10, 10, 10, 10, 10]

# Output: -1

# Explanation:

# The only value in nums is 10, so there is no second largest value, thus -1 is returned


def secondLargest(arr):
    if len(arr) <= 2:
        return -1
    
    largest = float('-inf')
    second = float('-inf')
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] > second and arr[i] < largest:
            second = arr[i]
        
    if second!= float('-inf'):
        return second
    else:
        return -1

print(secondLargest(nums))

    
    