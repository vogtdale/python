'''
Given an integer array nums, find the contiguous 
subarray (containing at least one number) 
which has the largest sum and return its sum.
'''

def maxSub(arr):
    max_ending = max_current = arr[0]

    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)

    return max_current

print(maxSub([-4, -2, -3, -4, 5]))
