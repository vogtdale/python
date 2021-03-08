"""
You are climbing a staircase. It takes n steps to reach the top.
"""
def stairs(n):
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return stairs(n-1) + stairs(n-2)

    if n == 1:
        return 1
    if n == 2:
        return 2

    path = [0 for i in range(n)]
    path[0], path[1] = 1, 2

    for i in range(2, len(path)):
        path[i] = path[i-1] + path[i-2]

    return path[-1] 

print(stairs(3))
