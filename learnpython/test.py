class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, newdata):
        if self.val:
            if newdata == self.val: return 'no duplicates allowed in binary search tree'
            if newdata < self.val:
                if self.left:
                    self.left.insert(newdata)
                else:
                    self.left = Node(newdata)
            else:
                if self.right:
                    self.right.insert(newdata)
                else:
                    self.right = Node(newdata)
        else:
            self.val = newdata

    def inOrder(self, lst):
        if self.left:
            self.left.inOrder(lst)
        lst.append(self.val)
        if self.right:
            self.right.inOrder(lst)
        return lst

    def preOrder(self, lst):
        lst.append(self.val)
        if self.left:
            self.left.preOrder(lst)
        if self.right:
            self.right.preOrder(lst)
        return lst

    def postOrder(self, lst):
        if self.left:
            self.left.postOrder(lst)
        if self.right:
            self.right.postOrder(lst)
        lst.append(self.val)
        return lst
    
    def depthFirstSearch_inorder(self):
        return self.inOrder([])
    def depthFirstSearch_preorder(self):
        return self.preOrder([])
    def depthFirstSearch_postorder(self):
        return self.postOrder([])


            
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
        

    
        