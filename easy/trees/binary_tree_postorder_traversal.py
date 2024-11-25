from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    arr = []

    def trav(node):
        if node:
            trav(node.left)
            trav(node.right)
            arr.append(node.val)

    trav(root)
    return arr
