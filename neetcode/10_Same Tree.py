from typing import Optional

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # Solution 1
        if not (p and q) or (p.val != q.val):
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        # Solution 2

        # stack = [[p,q]]
        # while stack:
        #     pnode, qnode = stack.pop()

        #     if not pnode and not qnode:
        #         continue

        #     if not (pnode and qnode) or (pnode.val != qnode.val):
        #         return False

        #     if pnode and qnode:
        #         stack.append([pnode.left,qnode.left])
        #         stack.append([pnode.right,qnode.right])

        # return True



