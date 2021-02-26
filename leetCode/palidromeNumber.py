def isPalidrome(x):
    y = str(abs(x))
    temp = int(y[::-1])

    if x == temp:
        return True
    else:
        return False
    
print(isPalidrome(121))
