from typing import List


def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    k = 0

    for num in nums:
        if num != val:
            nums[k] = num
            k += 1

    return k
