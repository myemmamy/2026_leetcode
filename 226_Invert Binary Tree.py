class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            tmp = node.right
            node.right = node.left
            node.left = tmp
            return node
        return dfs(root)
