def add_binary(a: str, b: str) -> str:
    st = str(bin(int(a, 2) + int(b, 2)))
    return st[2:]
