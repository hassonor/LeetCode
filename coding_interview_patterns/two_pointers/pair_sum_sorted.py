from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    Finds two indices of elements in a sorted list `nums` such that their sum equals the `target` value.

    The function assumes the input list is sorted in ascending order.

    Args:
        nums (List[int]): A list of integers sorted in ascending order.
        target (int): The target sum to find.

    Returns:
        List[int]: A list containing the indices of the two numbers whose sum equals the target.
                   If no such pair exists, returns an empty list.

    Example:
        >>> pair_sum_sorted([1, 2, 3, 4, 6], 6)
        [1, 3]

    Complexity Analysis:
        Time complexity: O(n), where n is the length of the input list. The two-pointer approach ensures a single pass through the list in the worst case.
        Space complexity: O(1), as only a constant amount of extra space is used.
    """
    # Initialize two pointers: left starts at the beginning, right starts at the end
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]  # Calculate the sum of the two pointer values

        if current_sum < target:
            # If the current sum is less than the target, move the left pointer to the right
            left += 1
        elif current_sum > target:
            # If the current sum is greater than the target, move the right pointer to the left
            right -= 1
        else:
            # If the current sum equals the target, return the indices
            return [left, right]

    # If no pair is found, return an empty list
    return []


# Example usage
if __name__ == "__main__":
    print(pair_sum_sorted([1, 2, 3, 4, 6], 6))  # Output: [1, 3]
