def convert_to_title(columnNumber):
    arr = []
    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        arr.append(chr(remainder + ord('A')))
        columnNumber //= 26

    return ''.join(reversed(arr))
