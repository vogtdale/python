'''
We are familiar with queue in our day to day life 
as we wait for a service. The queue data structure 
aslo means the same where the data elements are arranged 
in a queue. The uniqueness of queue lies in the way items are added 
and removed. The items are allowed at on end 
but removed form the other end. 
So it is a First-in-First out method. 
An queue can be implemented using python list where we can use the insert() and pop() methods to add and remove elements. 
Their is no insertion as data elements are always added at the end of the queue.
'''

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.append(dataval)
            return True
         
        return False

    def remove(self):
        if (len(self.queue) > 0):
            return self.queue.pop(0)
        return ("No element in the Queue")

    def peek(self):
        return print(self.queue)


        
    def size(self):
        return len(self.queue)  

if __name__ == '__main__':
    q = Queue()
    q.add("Monday")
    q.add("Tuesday")
    q.add("Wednesday")

    print("size queue", q.size())
    print("Iniatial queue: ")
    q.peek()

    print("Element to remove", q.remove())
    print("After deletion: ")
    q.peek()

    
