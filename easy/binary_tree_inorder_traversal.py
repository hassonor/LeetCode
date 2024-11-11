# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    arr = []

    def traverse(node):
        if node:
            traverse(node.left)
            arr.append(node.val)
            traverse(node.right)

    traverse(root)
    return arr
