"""
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True
        
