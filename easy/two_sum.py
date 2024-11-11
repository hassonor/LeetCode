from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
    comps = {}

    for ind, val in enumerate(nums):
        comp = target - val

        if comp in comps:
            return [comps[comp], ind]
        else:
            comps[val] = ind
