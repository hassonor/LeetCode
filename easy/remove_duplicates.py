from typing import List


def remove_duplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    k = 0

    for num in nums:
        if nums[k] != num:
            k += 1
            nums[k] = num

    return k + 1
