def is_happy(n):
    seen = set()
    number = n

    while number != 1:
        digits = [int(digit) for digit in str(number)]
        number = sum(map(lambda x: x ** 2, digits))
        if number not in seen:
            seen.add(number)
        else:
            return False

    return True
