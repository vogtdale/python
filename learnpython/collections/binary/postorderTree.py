'''
Post-Order Traversal 
1. check if the current node is empty / null
2. Traverse the left subtree by recursively calling the in-order function
3. Traverse the right subtree by recursively calling the in-order function
4. Display the data part of the root or current node

                      A
                    /   \
                   B     E
                  / \     \
                 C   D     F

Post-Order C,D,B,F,E,A
Post-Order 4-5-7-1-2-8-10

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
        if traversal_type == "postorder":
            return self.inorder_print(tree.root, "")
        else:
            print("Traversal Type " + str(traversal_type) + " 'snt supported")
            return False

    
    def inorder_print(self, start, travesal):
        '''Left->Right->Root'''

        if start: 
            travesal = self.inorder_print(start.left, travesal)
            travesal = self.inorder_print(start.right, travesal)
            travesal += (str(start.value) + "-")
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

print(tree.print_tree("postorder"))
        