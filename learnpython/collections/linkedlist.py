'''
A linked list is a sequence of data elements, 
which are connected together via links. 
Each data element contains a connection to another 
data element in form of a pointer. 
Python does not have linked lists in its standard 
library. We implement the concept of linked lists 
using the concept of nodes
'''

class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.next = None


class singelLinked:
    def __init__(self):
        self.head = None
    
    '''
    Singly linked lists can be traversed in only 
    forward direction starting form the first data element. 
    We simply print the value of the next data element 
    by assigning the pointer of the next node 
    to the current data element
    '''
    def printList(self):
        printval = self.head

        while printval is not None:
            val = printval.dataval
            printval = printval.next
            yield val

    '''
    This involves pointing the next pointer of the new data node
    to the current head of the linked list. 
    So the current head of the linked list becomes the second data element 
    and the new node becomes the head of the linked list.
    '''
    def insertAtbegining(self, newdata):
        newNode = Node(newdata)

        newNode.next = self.head
        self.head = newNode

    '''
    Inserting at the End

    This involves pointing the next pointer 
    of the the current last node of the linked list 
    to the new data node. 
    So the current last node of the linked list 
    becomes the second last data node and 
    the new node becomes the last node of the linked list.
    '''
    def insertAtEnd(self, newdata):
        newNode = Node(newdata)
        
        if self.head is None:
            self.head = newNode
            return 
        
        tail = self.head

        while tail.next:
            tail = tail.next
        tail.next = newNode

    '''
    This involves changing the pointer of a specific node 
    to point to the new node. 
    That is possible by passing in both the new node 
    and the existing node after which the 
    new node will be inserted. 
    So we define an additional class which will change 
    the next pointer of the new node 
    to the next pointer of middle node. 
    Then assign the new node to next pointer of 
    the middle node.
    '''
    def insertMiddle(self, middle, newdata):
        if middle is None:
            print("The mentioned node is absent")
            return
        newNode = Node(newdata)
        newNode.next = middle.next
        middle.next = newNode

    def searchval(self, val):
        for node in self.printList():
            if node == val:
                return True
        return False


    '''
    We can remove an existing node using the key 
    for that node. 
    we locate the previous node of the node which is to be deleted.
    Then, point the next pointer of this node 
    to the next node of the node to be deleted.
    '''
    def  deleteNode(self, key):
        #store head of Node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.dataval == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.dataval == key:
                break
            prev = temp
            temp = temp.next


        # if key was not present in linked list
        if temp == None:
            print("Not Present  in linked list")
            return 

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

        

def main():
    l = singelLinked()
    l.insertAtbegining("Sunday")
    l.insertAtEnd("Monday")
    l.insertAtEnd("Wednesday")
    l.insertMiddle(l.head.next, "Tuesday")
    l.insertAtEnd("Thursday")
    l.insertAtEnd("Friday")
    l.insertAtEnd("Saturday")

    for val in l.printList():
        print(val)

    searchterm = "Monday"
    term = searchterm.title()
    print("\nsearch term to look for in linkedList: " + f"{term}")
    print("\nWas the search term found in linked list: ", l.searchval(term))

    l.deleteNode("Monday")
    print("\nAfter removing node: ")
    for val in l.printList():
        print(val)

main()

