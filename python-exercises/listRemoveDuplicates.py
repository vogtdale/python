# Write a program (function!) that takes a list 
# and returns a new list that contains all the elements of the first list minus all the duplicates.

a = ["apple", "cherry", "pear", "orange", "bananna", "apple", "orange"]

def removeDuplicate(x):
    return list(set(x))


print(removeDuplicate(a))
