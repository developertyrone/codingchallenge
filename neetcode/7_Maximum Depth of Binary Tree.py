# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Solution 1 DFS(Depth first search), recursive
        # if not root:
        #     return 0

        # result = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # return result

        # Solution 2 BFS(Breadth first search), iterative
        # if not root:
        #     return 0

        # level = 0
        # q = deque([root])
        # while q:

        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     level += 1

        # return level

        # Solution 3 DFS(Depth first search), iterative
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                res = max(res, depth)

        return res

