from typing import Optional

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    #Solution1
        # nodes = []

        # if head.next is None:
        #     return None

        # if n == 0:
        #     return head.next

        # while head:
        #     nodes.append(head)
        #     head = head.next

        # if len(nodes) <= n:
        #     return nodes[0].next
        # else:
        #     nodes[len(nodes)-n-1].next = nodes[len(nodes)-n].next
        #     return nodes[0]

    #Solution2
        new_head = fast = slow = ListNode("sen", head)

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return new_head.next


