from typing import List


def plus_one(digits: List[int]) -> List[int]:
    num = int("".join(map(str, digits)))
    num += 1

    return [int(digit) for digit in str(num)]
