# A binary tree is data structure in which each node has 
# at most 2 children which are refered to as left child and right child 

class Node(self):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


#      10
#     /  \
#    7    8
#   / \
#  4   5

tree = BinaryTree(10)
tree.root.left = Node(7)
tree.root.right = Node(8)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(1)
tree.root.right.right = Node(2)


    