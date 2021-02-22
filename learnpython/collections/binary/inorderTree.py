'''
In-Order Traversal 
1. check if the current node is empty / null
2. Traverse the left subtree by recursively calling the in-order function
3. Display the data part of the root or current node
4. Traverse the right subtree by recursively calling the in-order function

                      A
                    /   \
                   B     E
                  / \     \
                 C   D     F

In-Order C,B,D,A,E,F 
In order 4-7-5-10-1-8-2-


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
        if traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        else:
            print("Traversal Type " + str(traversal_type) + " 'snt supported")
            return False

    
    def inorder_print(self, start, travesal):
        '''Left->Root->Right'''

        if start: 
            travesal = self.inorder_print(start.left, travesal)
            travesal += (str(start.value) + "-")
            travesal = self.inorder_print(start.right, travesal)
        return travesal

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

print(tree.print_tree("inorder"))
        