"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp_val = self.head

        while temp_val is not None:
            print(temp_val.val) 
            temp_val = temp_val.next

    def addTolist(self, newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def removeNode(self, head):
        head_val = self.head

        if head_val is not None:
            if head_val.val == head:
                self.head = head_val.next
                head_val = None
                return
        while head_val is not None:
            if head_val.val == head:
                break

            prev = head_val
            head_val = head_val.next

        if head_val == None:
            return 
        
        prev.next = head_val.next
        head_val = None







l = linkedList()

l.addTolist(1)
l.addTolist(2)
l.addTolist(3)
l.addTolist(4)
l.addTolist(5)
l.addTolist(5)

l.removeNode(5)
l.printList()
    