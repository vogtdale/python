def isPalidrome(x):
    temp = str(x)

    rev = str(temp[::-1])

    if x == rev:
        return True
    else:
        return False

print(isPalidrome("racecar"))
