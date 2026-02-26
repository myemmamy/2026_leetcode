# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def helper(node,path): 
            if not node:
                return
            if node.val == targetSum:
                self.res += 1
            for x in path:
                if node.val == targetSum - x:
                    self.res += 1
            path = [x + node.val for x in path]
            path.append(node.val)
            if node.left:
                helper(node.left,path)
            if node.right:
                helper(node.right,path)
            #path.pop() not needed since path is new instance ?
        helper(root,[])
        return self.res
