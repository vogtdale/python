'''
collections are ordered or 
un oredered group of  elements
'''

# list can store != data types 
# it's an ordered goupe of elemenst 
# the order in which we enter things in collection is maintained
# list are mutable fruits[0] = "coco" will replace the value apple

fruits = ["apple", "pear", "cherry", "melon"]  # the variable fruits stores a reference to the list the items ar e actually stored somewhere else 

fruits.extend(["water-mellon", "bannana", "orange"])

# to get the last index in a list 
# look at the length of the list - 1

for loop in fruits:
    print(loop)

print(len(fruits))  # retusrns the number of items in a list
print(fruits)
fruits.pop(0) # remove and return item at index(default is the last of the list)
print(fruits)


