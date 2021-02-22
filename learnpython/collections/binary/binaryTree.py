class Node:
   def __init__(self, value):
       self.value = value
       self.right = None  #ptr to left node child
       self.right = None #ptr to right node child
      

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
