def my_sqrt(x: int) -> int:
    left, right = 1, x // 2 + 1

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    return right
