# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not.
#  If the array is sorted then return True, Else return False.

def isSorted(arr):
    sorted = False
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            sorted = True
        else:
            sorted = False
    return sorted


print(isSorted([1,2,3,4,5,6,8,7]))