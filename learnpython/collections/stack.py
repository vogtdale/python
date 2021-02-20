'''
In the english dictionary the word stack means arranging objects on over another. 
It is the same way memory is allocated in this data structure. 
It stores the data elements in a similar fashion as a bunch of plates are stored one above another in the kitchen. 
So stack data structure allows operations at one end wich can be called top of the stack. We can add elements or remove elements only form this en dof the stack.
In a stack the element insreted last in sequence will come out first as we can remove only from the top of the stack. Such feature is known as Last in First Out(LIFO) feature. The operations of adding and removing the elements is known as PUSH and POP. In the following program we implement it as add and and remove functions. We dclare an empty list and use the append() and pop() methods to add and remove the data elements.
'''

book_shelf = []

book_shelf.append("mobby dick")
book_shelf.append("great expectations")
book_shelf.append("anne frank")

print(book_shelf)

# remove the last item 
book_shelf.pop()
if not book_shelf:
    book_shelf[-1]

print("After removing book from stack:\n",book_shelf)


