# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def helper(node):
            prev = None
            cur = node
            if not node:
                return
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                prev = cur
                cur = cur.left
                prev.right = cur
                prev.left = None
                helper(cur)
            else: 
                if not stack:
                    return
                tmpnode = stack.pop()
                prev = cur
                cur = tmpnode
                prev.right = cur
                prev.left = None
                helper(cur)
        helper(root)

#recursion
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            if right:
                return right
            if left:
                return left
            return node
        dfs(root)
