from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None

    cur_a = headA
    cur_b = headB

    while cur_a != cur_b:
        cur_a = cur_a.next if cur_a is not None else headB
        cur_b = cur_b.next if cur_b is not None else headA

    return cur_a
