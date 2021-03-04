def searchPosition(arr, target):

    if target in arr:
        return arr.index(target)

    else:
        for i in range(len(arr)):
            if arr[i] > target:
                return i
        return arr


l = [1,2,3,4,5,6]
t= 4
print(searchPosition(l,t))
