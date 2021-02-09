#Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# When we say that dictionaries are unordered, it means that the items does not have a defined order, you cannot refer to an item by using an index


#Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets:
print(thisdict["brand"]) # or 

x = thisdict.get("model")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
print(thisdict.keys())

# Update the "year" of the car by using the update() method:
print(thisdict.update({"year": "2020"}))

# The values() method will return a list of all the values in the dictionary.
print(thisdict.values())

# the items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())

