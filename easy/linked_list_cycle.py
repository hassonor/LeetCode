from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    slow_head = head
    fast_head = head

    while fast_head is not None and fast_head.next is not None:
        slow_head = slow_head.next
        fast_head = fast_head.next.next

    return slow_head == fast_head
