# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, 
# all with different qualities and usage.
# A set is a collection which is both unordered 
# and unindexed No duplicate members..
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.

x = set((0,1,2,3,4)) # use constructor if we use x = {} creaets a dictonary
y = set((2,6,8,9))
print(x)
x.add(7)
x.remove(4)
print(x)

# check if something is in  a set 
print(3 in x)  # happens at const time faster than list

print(x.union(y)) # cocanantes both sets
print(x.difference(y))