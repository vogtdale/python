'''
Tuple items are ordered, unchangeable, 
and allow duplicate values.
tuples are non mutable
cannot remove nor append 
if want to change an them must be redifined
'''

x = ("cats", "dogs", "rats")

# acess items in a tuble 
print(x[0])

# update tuple or remove cant be done unmutable
# neesds to be redifined
y = list(x)
y.pop(0)
print("after redfine and remove in tuple", y)



