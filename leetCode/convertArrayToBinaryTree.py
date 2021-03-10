# Given an integer array nums 
# where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which 
# the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(left, right):
            if right < left: 
                return None
            
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node

        return helper(0, len(nums) - 1)
       
        
