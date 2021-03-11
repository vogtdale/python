"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

        Input: root = [3,9,20,null,null,15,7]
        Output: 2

"""
class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
            
        left = self.minDepth(root.left)
        right  = self.minDepth(root.right)

        if root.right and root.right == None:
            return 1
        
        if root.left == None:
            return right + 1

        if root.right == None:
            return left + 1

        return min(left, right) + 1
