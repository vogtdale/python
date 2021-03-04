'''
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. 
If the last word does not exist, return 0.
'''

def LengthOfword(string):
    copy = string.strip()
    count = 0

    for i in range(len(copy)):
        if copy[i] == " ":
            count = 0
        else:
            count += 1
    return count

print(LengthOfword("hellow world"))
