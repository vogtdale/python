'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
'''

def RemoveElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
            i-=1
        else:
            i += 1    

    return nums


arr = [1,2,3,4,5,4]
val = 4
print(RemoveElement(arr, val))
