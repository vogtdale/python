def isValide(string):
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    for char in string:
        if char in pairs.keys():
            stack.append(char)
        elif len(stack) > 0 and pairs.get(stack[-1]) == char:
            stack.pop()
        else: 
            return False

    return len(stack) == 0

s = "()[]{}"
print(isValide(s))
