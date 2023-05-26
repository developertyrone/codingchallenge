Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Solution 1
        # balance = [True]
        # def dfs(root):
        #     if not root:
        #         return 0
        #
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #
        #     if abs(left - right) > 1:
        #         balance[0] = False
        #
        #     return 1 + max(left, right)
        #
        # dfs(root)
        # return True if balance[0] != False else False
        #

        # Solution 2


        def dfs(root):
            if not root: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]

