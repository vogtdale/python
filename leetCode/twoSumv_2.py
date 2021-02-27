'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

'''


def twoSum(arr, target):  # returns a list
    h={}

    for i, item in enumerate(arr):
        remainder = target - item

        if remainder not in h:
            h[item] = i
        else:
            return [h[remainder], i] 

l = [2,4,5,7]
target = 7

print(twoSum(l, target))
