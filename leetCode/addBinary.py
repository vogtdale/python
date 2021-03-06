def addBinary(a,b):
    i=len(a) -1
    j=len(b) -1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        total = carry
        if i >= 0:
            total += int(a[i])
            i-=1
        if j >= 0:
            total += int(b[j])
            j-=1

        result = str(total % 2) + result
        carry = total // 2

    if carry == 1:
        result = "1" + result
    return result

a="11"
b="1"
print(addBinary(a,b))

        