def is_palindrome(self, s: str) -> bool:
    st = "".join(char for char in s if char.isalnum()).lower()
    return st == st[::-1]
