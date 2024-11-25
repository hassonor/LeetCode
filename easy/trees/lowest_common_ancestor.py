"""
התרגיל מבקש למצוא את האבא המשותף הקרוב ביותר (Lowest Common Ancestor, LCA) של שני צמתים בעץ בינארי.
בוא נפרט את זה:

"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    # אם הגעת לצומת ריק או לצומת שמכיל את אחד מהצמתים
    if root is None or root == p or root == q:
        return root

    # חיפוש בצד שמאל
    left = lowest_common_ancestor(root.left, p, q)
    # חיפוש בצד ימין
    right = lowest_common_ancestor(root.right, p, q)

    # אם מצאנו תשובות משני הצדדים, השורש הוא האבא המשותף
    if left and right:
        return root

    # אחרת נחזיר את מה שמצאנו (או כלום, או תשובה משמאל/ימין)
    return left if left else right
