class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {v:i for i,v in enumerate(inorder)}
        postindex = len(postorder) - 1
        def dfs(l,r):
            if l > r:
                return None
            nonlocal postindex
            val = postorder[postindex]
            postindex -= 1
            root = TreeNode(val)
            mid = d[val]
            root.right = dfs(mid+1,r)
            root.left = dfs(l,mid-1)
            return root
        return dfs(0,len(inorder)-1)
