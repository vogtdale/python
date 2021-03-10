"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every 
node differ in height by no more than 1.

        Input: root = [3,9,20,null,null,15,7]

        Output: true

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        def helper(node):
            if not node:
                return (0,True)
            
            l_height, l_balance = helper(node.left)
            r_height, r_balance = helper(node.right)

            return (max(l_height, r_height) + 1, l_balance and r_balance and abs(l_height - r_height) <= 1)
        
        return helper(root)[1]
