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


    """
    result = ""
    carry = 0

    a = list(a)
    b = list(b)

    while a or b or carry == 1:
        if a:
            carry += int(a.pop())

        if b: 
            carry += int(b.pop())
        
        result += str(carry % 2)
        carry = carry // 2
    
    return result[::-1]
    """

a="11"
b="1"
print(addBinary(a,b))

        