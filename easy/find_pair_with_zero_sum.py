def find_pair_with_zero_sum(arr):
    seen = set()

    for num in arr:
        if -num in seen:
            return (num, -num)
        seen.add(num)

    return -1
