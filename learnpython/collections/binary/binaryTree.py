'''
A Binary Tree is a non-linear data structure 
that is used for searching and data organization. 
A binary tree is comprised of nodes. 
Each node being a data component, 
one a left child and the other the right child. 
'''
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.left = None  #ptr to left node child
        self.right = None #ptr to right node child


    
    #insert
    def insert(self, newdata):
        if self.dataval:
            if newdata == self.dataval: return 'no duplicates allowed in binary search tree'

            # check if value to be inserted < currentNode's value
            # If the node to be inserted is less than the parent then 'insert left'.
            if newdata < self.dataval:
                # check if there is a left node to currentNode if true then recurse
                if self.left:
                    self.left.insert(newdata)
                else:
                    self.left = Node(newdata)

            # If the node to be inserted is more than the parent then 'insert right'.  
            else:
                if self.right:
                    self.right.insert(newdata)
                else:
                    self.right = Node(newdata)
        else:
            self.dataval = newdata

    
    '''
    Traversals
    Since a binary tree is a non-linear data structure, 
    there is more than one way to traverse through the tree data. 
    Let’s look at the various types of traversals in a binary tree, 
    including inorder traversal, 
    preorder traversal, and 
    postorder traversal.
    '''

    # In order means first left child, then parent, at last right child
    def inorderTraversal(self, lst):
        if self.left:
            self.left.inorderTraversal(lst)
        lst.append(self.dataval)
        if self.right:
            self.right.inorderTraversal(lst)
        return lst

            
    
    # Pre order means first parent, then left child, at last right child
    def preorderTraversal(self, lst):
        lst.append(self.dataval)
        if self.left:
            self.left.preorderTraversal(lst)
        if self.right:
            self.right.preorderTraversal(lst)
        return lst

    # Post order means first left child, then right child , at last parent
    def postorderTraversal(self, lst):
        if self.left:
            self.left.postorderTraversal(lst)
        if self.right:
            self.right.postorderTraversal(lst)
        lst.append(self.dataval)
        return lst


    def depthFirstSearch_inorder(self):
        return self.inorderTraversal([])
    def depthFirstSearch_preorder(self):
        return self.preorderTraversal([])
    def depthFirstSearch_postorder(self):
        return self.postorderTraversal([])

    

    
bst = Node()    
bst.insert(7)
bst.insert(4)
bst.insert(9)
bst.insert(0)
bst.insert(5)
bst.insert(8)
bst.insert(13)

#          7
#        /  \
#      /     \
#     4        9
#    / \      /  \
#   0   5    8    13

    
print('IN order: ',bst.depthFirstSearch_inorder())
print('pre order: ',bst.depthFirstSearch_preorder())
print('post order: ',bst.depthFirstSearch_postorder())

