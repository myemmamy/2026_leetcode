class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        cur = root
        stack = deque()
        stack.append(cur)
    
        while stack:
            l = len(stack)
            v = 0
            for i in range(l):
                node = stack.popleft()
                v += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(v/l)
        return ans
