class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = [False] * n
        ans = []
        path = []
        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(n):
                if not seen[i]:
                    path.append(nums[i])
                    seen[i] = True
                    dfs() 
                    path.pop()
                    seen[i] = False
        dfs()
        return ans 
    
