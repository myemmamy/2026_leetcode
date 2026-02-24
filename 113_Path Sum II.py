# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def helper(node,path,tmpSum):
            if not node:
                return
            path.append(node.val)
            tmpSum = tmpSum + node.val
            if not node.left and not node.right:
                if tmpSum == targetSum:
                    paths.append(path.copy())
            helper(node.left, path, tmpSum)
            helper(node.right, path, tmpSum)
            path.pop()
        helper(root,[],0)
        return paths
