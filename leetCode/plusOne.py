"""
Given a non-empty array of decimal digits representing 
a non-negative integer, increment one to the integer.
"""

def plusOne(digits):

    s = ""
    # take the array and append each character into a string to make it string
    for i in digits:
        s += str(i)
    # then convert the string to an integer, then increase the number by 1
    s = int(s)
    s += 1
    s = str(s)
    newlist = []
    # then split each digit and make another array
    for i in s:
        newlist.append(int(i))

    return newlist

l = [1,2,3]

print(plusOne(l))
