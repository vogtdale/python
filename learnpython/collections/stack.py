'''
In the english dictionary the word stack means arranging objects on over another. 
It is the same way memory is allocated in this data structure. 
It stores the data elements in a similar fashion as a bunch of plates are stored one above another in the kitchen. 
So stack data structure allows operations at one end wich can be called top of the stack. We can add elements or remove elements only form this en dof the stack.
In a stack the element insreted last in sequence will come out first as we can remove only from the top of the stack. Such feature is known as Last in First Out(LIFO) feature. The operations of adding and removing the elements is known as PUSH and POP. In the following program we implement it as add and and remove functions. We dclare an empty list and use the append() and pop() methods to add and remove the data elements.
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True

        else:
            return False

    def remove(self):
        if (len(self.stack) <= 0):
            return  ("No element in the Stack")
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]



if __name__ == "__main__":
    s= Stack()
    s.add("Monday")
    s.add("Tuesday")
    s.add("Wednesday")

    print(s.peek())
    temp = s.peek()
    print(f"\nAfter deleting: {temp}", s.remove())
    print(s.peek())
    
    

