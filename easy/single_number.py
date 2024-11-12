from typing import List


def singleNumber(nums: List[int]) -> int:
    arr = {}

    for ind, num in enumerate(nums):
        if num in arr:
            arr.pop(num, None)
        else:
            arr[num] = 1

    return next(iter(arr.keys()))
