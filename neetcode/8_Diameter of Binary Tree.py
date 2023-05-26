# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Solution 1, O(n^2)
        #     if not root:
        #         return 0
        #     res = 0
        #     stack = [root]
        #     while stack:
        #         node = stack.pop()

        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        #         res = max(res,self.nodeDepth(node.left) + self.nodeDepth(node.right))

        #     return res

        # def nodeDepth(self, root: Optional[TreeNode]) -> int:
        #     stack = [[root, 1]]
        #     res = 0
        #     while stack:
        #         node, depth = stack.pop()

        #         if node:
        #             stack.append([node.left, depth + 1])
        #             stack.append([node.right, depth + 1])
        #             res = max(res, depth)

        #     return res
        # Solution 2, O(n)
        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]
