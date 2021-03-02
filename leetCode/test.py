class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def linkedList(self):
        self.head = None

    def printList(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.val)
            print_val = print_val.next



class solution(object):
    def mergeTwoList(self,l1,l2):
        dummyNode = output = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next

            output = output.next

        if l1: output.next = l1
        if l2: output.next = l2
    
        return dummyNode.next


l1 = [1,2,3]
l2 = [1,3,4]
linked = ListNode()
linked.head.val = linked.mergeTwoList(l1,l2)

print(linked.head.val)

