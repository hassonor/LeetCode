def find_missing_ranges(nums, lower, upper):
    prev = lower - 1
    nums.append(upper + 1)
    arr = []

    for num in nums:
        if num - prev > 1:
            arr.append([prev + 1, num - 1])
        prev = num

    return arr
