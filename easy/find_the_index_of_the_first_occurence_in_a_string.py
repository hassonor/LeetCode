def str_str(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    for ind, val in enumerate(haystack):
        if ind + len(needle) <= len(haystack):
            if needle == haystack[ind: ind + len(needle)]:
                return ind

    return -1
