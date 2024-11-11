def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    str_x = str(x)

    return str_x == str_x[::-1]
