'''
Two dimensional array is an array within an array. 
It is an array of arrays. In this type of array the position 
of any data element is referred by two indices instead of one. 
So it represents a table with rows and columns of data.
'''

from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# The data elements in two dimesnional arrays 
# can be accessed using two indices. 
# One index referring to the main or parent array 
# and another index referring to the position 
# of the data element in the inner array. 
# If we mention only one index then the entire 
# inner array is printed for that index position. 
print(T[0])
print(T[1][2])


# To print out the entire two dimensional 
# array we can use python for loop. We use end of line to print out the values in different rows.

for row in T:
    for col in row:
        print(col, end= " ")
    print()
