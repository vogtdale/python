'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
basicly two ptr* solution
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def mergeSortedList(self, l1, l2):
        dummy = ListNode()

        while l1 and l2: # none null
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next

            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        # add elemnts of still remaing list
        if l1: dummy.next = l1
        if l2: dummy.next = l2

        return dummy.next # which is the head


l1 = [1,2,3,4]
l2 = [2,4,5,6]

obj = ListNode()
print(obj.mergeSortedList(l1,l2))

