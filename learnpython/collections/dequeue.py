'''
A double-ended queue, or deque, 
supports adding and removing elements from either end. 
The more commonly used stacks and queues are degenerate forms 
of deques, where the inputs and outputs are restricted to 
a single end.
'''

from collections import deque

data = deque()

data.append("Mon")
data.append("Tue")
data.append("Wend")

print(data)

data.appendleft("Sund")
print(data)

data.popleft()
data.pop()

if not data:
    data[0]
print("After removing elements from queue \n")
print(data)


