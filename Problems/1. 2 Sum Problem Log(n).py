def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

# Example usage
numbers = [2, 3, 4, 7, 11, 15]  # must be sorted
target = 9
print(two_sum_sorted(numbers, target))
