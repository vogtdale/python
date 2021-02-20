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

data = []

# Queue
data.append(1)
data.append(2)
data.append(3)

print(data)

# Dequeue
data.pop(0)  # First-in-First out method
if not data:
    data[0]
print(data)
