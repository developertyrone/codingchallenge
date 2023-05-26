from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            temp = head.next  # var = 2->3,4,5 | head = 1->2,3,4,5
            # var = 3->4,5 | head = 2->3,4,5
            head.next = dummy  # head.next = (1,None), break the chain
            # head.next = (2,(1,None))
            dummy = head  # dummy = (1,None), extract the val
            # dummy = (2,(1,None))
            head = temp  # head = 2->3,4,5
            # head = 3->4,5

        return dummy