'''
given a signed 32-bit integer x, 
return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

def reverse(x):
    temp = str(abs(x))

    reverse = int(temp[::-1])

    # If reversing x causes the value 
    # to go outside the signed 32-bit integer
    # A signed integer is a 32-bit datum that encodes an integer 
    # in the range [-2147483648 to 2147483647].
    if reverse > 2**31:
        return 0
    
    if x > 0:
        return reverse
    else:
        reverse * -1
    
print(reverse(12345))

