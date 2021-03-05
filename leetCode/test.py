def searchPstition(arr, target):
    position=0

    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            if target < arr[i]:
                return i
            else:
                position = i + 1
    return position

l=[1,2,3,4,5,6,7]
t=4
print(searchPstition(l,t))
