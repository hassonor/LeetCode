from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    if root.left is None and root.right is None:
        return root.val == targetSum

    targetSum -= root.val

    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
