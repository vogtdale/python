class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
# Class to create a Doubly Linked List
class DoublyLinkedList:
 
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def insertAtbegining(self, new_data):
 
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)
 
        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head
 
        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node
 
        # 5. move the head to point to the new node
        self.head = new_node

    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def insertAtEnd(self, new_data):
 
        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)
 
        # 3. This new node is going to be the last node,
        # so make next of it as None
        # (It already is initialized as None)
 
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node
 
        # 7. Make last node as previous of new node
        new_node.prev = last
 
        return
 
    # Given a node as prev_node, insert a new node after
    # the given node
    def insertNodeAfter(self, prev_node, new_data):
 
        # 1. Check if the given prev_node is None
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
 
        # 2. allocate new node
        # 3. put in the data
        new_node = Node(new_data)
 
        # 4. Make net of new node as next of prev node
        new_node.next = prev_node.next
 
        # 5. Make prev_node as previous of new_node
        prev_node.next = new_node
 
        # 6. Make prev_node ass previous of new_node
        new_node.prev = prev_node
 
        # 7. Change previous of new_nodes's next node
        if new_node.next:
            new_node.next.prev = new_node

    def insert_before(self, before_node, new_data): # Inserting a new node before a given node
        # 1. Check if the given prev_node is None
        if before_node == None:
            print("Given node is empty")

        # 2. allocate new node
        # 3. put in the data
        new_node = Node(new_data)

        # 4. Make prev of new node as prev of before node
        new_node.prev = before_node.prev

        # 5. Make before_node as previous of new_node
        before_node.prev = new_node
        
 
        # 6. Make before_node as previous of new_node
        new_node.next = before_node
        
        if new_node.prev != None:
            new_node.prev.next = new_node
      
        if before_node == self.head: # checks whether new node is being added before the first element
            self.head = new_node # makes new node the new head

    def deleteNodeAtStart(self):

        if self.head != None:
            temp = self.head
            self.head = temp.next 
            temp = None

            if self.head != None:
                self.head.prev = None
    def DeleteAtStart(self):
        temp = self.head
        if temp is None:
            print("The Linked list is empty, no element to delete")
            return 
        if temp.next != None:
            self.head = temp.next
            temp = None
            return
        self.head = temp.next
        temp.prev = None

    def delete_at_end(self):
        temp = self.head
        # Check if the List is empty
        if temp is None:
            print("The Linked list is empty, no element to delete")
            return 
        if temp.next is None:
            self.head = temp.next
            temp = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
    

    def printList(self):

        printval = self.head
        while printval != None:
            val = printval.data
            printval = printval.next
            yield val


if __name__ == "__main__":
    l = DoublyLinkedList()
    l.insertAtbegining("Sunday")
    l.insertAtEnd("Monday")
    l.insertNodeAfter(l.head.next, "Wednesday")
    l.insert_before(l.head.next.next, "Tuesday")

    for val in l.printList():
        print(val)


