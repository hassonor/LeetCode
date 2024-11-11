def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for _ in range(2, n + 1):
        cur = one + two
        two = one
        one = cur

    return one
