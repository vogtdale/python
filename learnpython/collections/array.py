from array import *

# create array 

array = array("i", [10, 20, 30, 40, 50])

for loop in array:
    print(loop)


# access array element
print(array[0])

#  insert opertaion 
array.insert(0, 60)

print("array after insertion: ", array)