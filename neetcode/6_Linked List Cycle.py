# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution 1
        # travels = []
        # while head:
        #     if head not in travels:
        #         travels.append(head)
        #     else:
        #         return True
        #     head = head.next
        # return False

        # Solution 2
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False