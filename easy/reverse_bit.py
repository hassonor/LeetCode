def reverse_bits(n):
    number = 0
    for _ in range(32):
        number = (number << 1 | (n & 1))
        n >>= 1

    return number
