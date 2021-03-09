def sqrt(x):
    low = 0
    high = x

    while low < high:
        mid = (low+high) // 2
        mid_sqrt = mid * mid

        if mid_sqrt <= x:
            low = mid + 1
        else:
            high = mid - 1
        return low - 1
