# Given the root of a binary tree, 
# check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None):
            return True
        return self.symmetric(root,root.left,root.right)
    
    def symmetric(self,root,left,right):

        if(left == None and right == None):
            return True
        if(left == None or right == None):
            return False
        if(left.val!=right.val):
            return False
        return self.symmetric(root,left.left,right.right) and   self.symmetric(root,left.right,right.left)
