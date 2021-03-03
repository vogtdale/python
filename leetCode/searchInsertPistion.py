'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''

def search(nums, target):
    index = 0
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            if target < nums[i]:
                return i
            else:
                index = i+1
    return index

nums = [1,3,4,5,6]
t = 2
print(search(nums,t))
