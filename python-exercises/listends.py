# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def listEnds():
    newList= [x for x in a if x == 5 or x == 25]
    return newList

print(listEnds())
