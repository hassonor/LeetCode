def title_to_number(columnTitle):
    total = 0

    for s in columnTitle:
        total = total * 26 + (ord(s) - ord('A') + 1)

    return total
