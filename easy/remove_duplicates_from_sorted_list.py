from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        seen_vals = set()
        seen_vals.add(head.val)
        cur = head

        while cur.next is not None:
            if cur.next.val in seen_vals:
                cur.next = cur.next.next
            else:
                seen_vals.add(cur.next.val)
                cur = cur.next

        return head
