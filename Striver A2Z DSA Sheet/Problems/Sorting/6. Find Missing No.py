#  Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.


def missingNumber(nums) -> int:
        nums = sorted(nums)
        # missing_number = -1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                return nums[i] + 1
        return len(nums)
        
print(missingNumber([9,6,4,2,3,5,7,0,1]))
print(missingNumber([0,1]))