def removeElements(arr, val):
    length = len(arr)
    i = 0

    while length > i:
        if arr[i] == val:
            del arr[i]
            length -= 1
        else:
            i += 1
    return arr

l=[1,2,3,4,5,6,7]
t=4
print(removeElements(l,t))
