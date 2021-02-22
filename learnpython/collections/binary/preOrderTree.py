
'''
Pre-Order Traversal 
1. check if the current node is empty
2. Diplay the data part of the root or current node
3. Traverse the left subtree by recursively calling the pre-order function
4. Traverse the right subtree by recursively calling the pre-order function

                      A
                    /   \
                   B     E
                  / \     \
                 C   D     F

Pre-Order A,B,C,D,E,F 

'''

# *************** Implementation************ #

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

        else:
            print("Traversal Type " + str(traversal_type) + " Is not Supported")
            return False

    # start is the node that will be updated on every recursive call  
    # traversal is a string that will be printed out to screen it will b eupdated on every recursive call
    def preorder_print(self, start, traversal):  
        '''ROOT->Left->Right'''

        if start:  # check if node givenin this recursive call is none/empty 
            #if not none
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left , traversal)  # recursive call
            traversal = self.preorder_print(start.right, traversal)  # recursive call
        return traversal

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

print(tree.print_tree("preorder"))
