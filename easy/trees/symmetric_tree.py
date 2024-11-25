from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(left, right):

        if left is None or right is None:
            return left == right
        elif left.val != right.val:
            return False

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)
