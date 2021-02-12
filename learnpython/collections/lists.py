'''
collections are ordered or 
un oredered group of  elements
'''

# list can store != data types 
# it's an ordered goupe of elemenst 
# the order in which we enter things in collection is maintained
# list are mutable fruits[0] = "coco" will replace the value apple

fruits = ["apple", "pear", "cherry", "melon"]  # the variable fruits stores a reference to the list the items ar e actually stored somewhere else 


# Access List items or indexing
print(fruits[0])

#change list item change value of a specific item 
fruits[1] = "coco"
print(fruits)

# add list items with append or extend 
fruits.append("orange")
print("list after append: ", fruits)

basket = [1,2,3]
basket.extend(fruits)
print("after extends: ", basket)

# remove list removes the specified item.
fruits.remove("orange")
print("after remove action: ", fruits)
fruits.pop(1)
print("After pop methode: ", fruits)


# loop through a list of items with for loop 
for loop in fruits:
    print("loop through the items: ", loop)

# loop through a list by refering there index numbers 
for loop in range(len(fruits)):
    print("loop through items index", fruits[loop])
    print("loop through items index number", loop)

# list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
list = ["apple", "pear", "cherry", "melon", "apple"]
newList = [x for x in list]
print("list comprehsion", newList)



