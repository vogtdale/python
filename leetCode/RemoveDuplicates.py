'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
'''
def removeDuplicates(nums):
    i = 0

    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return nums

nums = [1,1,2,3,3,4,5]
print(removeDuplicates(nums))
