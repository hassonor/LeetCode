def is_valid(self, s: str) -> bool:
    pars = {"}": "{", "]": "[", ")": "("}
    arr = []

    for ch in s:
        if ch in pars:
            if not arr or pars[ch] != arr.pop():
                return False

        else:
            arr.append(ch)

    return not arr
