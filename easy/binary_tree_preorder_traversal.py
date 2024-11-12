from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    arr = []

    def pre_traverse(node):
        if node:
            arr.append(node.val)
            pre_traverse(node.left)
            pre_traverse(node.right)

    pre_traverse(root)
    return arr
