'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

def longestCommonPrefix(arr): # arr of strings
    # check if arr is empty if empty return ""
    if len(arr) == 0:
        return ""

    #check if arr contains on word
    if len(arr) == 1:
        return arr[0] # retrun the index of that word

    # find the shortest word in arr 
    short_str = min(arr, key=len)

    for i, char in enumerate(short_str):
        for c in arr:
            if c[i] != char:
                return short_str[:i]
    return short_str

l = ["flower","flow","flight"]
print(longestCommonPrefix(l))
