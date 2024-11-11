# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    a, b = [], []

    def traverse(node, arr):
        if node:
            arr.append(node.val)
            traverse(node.left, arr)
            traverse(node.right, arr)

        else:
            arr.append(None)

    traverse(p, a)
    traverse(q, b)
    return a == b
