def majority_element(nums):
    vals = {}
    size = len(nums) // 2
    for num in nums:
        if num in vals:
            vals[num] += 1
        else:
            vals[num] = 1
        if vals[num] > size:
            return num
