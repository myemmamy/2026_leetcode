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

#2
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        tmp = root.right
        root.right = root.left
        root.left = tmp
        return root

