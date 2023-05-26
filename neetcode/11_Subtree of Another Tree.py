from typing import Optional
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Solution 1
        # stack = [root]
        # while stack:
        #     node = stack.pop()

        #     if node:
        #         if node.val == subRoot.val:
        #             if self.sameTree(node, subRoot):
        #                 return True
        #         stack.append(node.left)
        #         stack.append(node.right)

        # return False

        # Solution 2
        if not root: return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not (p and q) or p.val != q.val:
            return False

        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))