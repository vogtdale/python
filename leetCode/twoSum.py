'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

'''

from array import *


def two_sum_hash_table(arr, total):
    hash_table = {}

    for i in range(len(arr)):
        complement = total - arr[i]
        print("complement ", complement)
        if complement in hash_table:
            return (i, hash_table[complement])

        else:
            hash_table[arr[i]] = i
    return None

h=[2,4,5,7]
target = 9
print(two_sum_hash_table(h, target))
