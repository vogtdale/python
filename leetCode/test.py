def removeElement(nums, val):
    temp = len(nums)

    i = 0

    while temp > i:
        if nums[i] == val:
            del nums[i]
            temp -= 1
        else:
            i += 1
    return nums

arr = [1,2,3,4,5,4]
val = 4
print(removeElement(arr, val))
