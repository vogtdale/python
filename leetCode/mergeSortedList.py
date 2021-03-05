'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
basicly two ptr* solution
'''

# Definition for singly-linked list.
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

def mergeList(l1,l2):
    dummy = Node()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2= l2.next

        tail = tail.next

    if l1: tail.next = l1
    if l2: tail.next = l2

    return dummy.next



lA = linkedList()
lB = linkedList()

lA.addTolist(1)
lA.addTolist(4)
lA.addTolist(5)

lB.addTolist(2)
lB.addTolist(3)
lB.addTolist(6)

lA.head = mergeList(lA.head, lB.head)

lA.printList()

