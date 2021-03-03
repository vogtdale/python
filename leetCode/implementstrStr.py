def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1
        
h = "hello"
n = "ll"
print(strStr(h,n))
