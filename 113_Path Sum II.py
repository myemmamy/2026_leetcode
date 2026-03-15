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
            path.pop() #只pop一次，而不是左右子树各pop一次，因为一层做了一次append，也只做一次pop。 左子树自己会pop自己的节点，右子树也会pop自己的节点
        helper(root,[],0)
        return paths

# 没有做路径path 回溯，而是用了新的path 变量 ，不会污染后续操作
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node,path):
            if not node:
                return
            new_path = path + [node.val]
            if not node.left and not node.right:
                if node.val == targetSum - sum(path):
                    paths.append(new_path)
                    return
            if node.left:
                dfs(node.left,new_path)
            if node.right:
                dfs(node.right,new_path])
        dfs(root,[])
        return paths
#0315

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        total = 0
        def dfs(node,subtotal):
            if not node:
                return
            subtotal += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if subtotal == targetSum:
                    ans.append(path[:])
            dfs(node.left,subtotal)
            
            dfs(node.right,subtotal)
            path.pop()
        dfs(root,0)
        return ans
