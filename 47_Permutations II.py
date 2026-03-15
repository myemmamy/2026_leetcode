class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []
        seen = [False] * n
        def dfs():
            if len(nums) == len(path):
                ans.append(path[:])
                return
            for i in range(n):
                if seen[i] or (i > 0 and nums[i] == nums[i-1] and not seen[i-1]):
                    continue
                path.append(nums[i])
                seen[i] = True
                dfs()
                path.pop()
                seen[i] = False
        dfs()
        return ans
            
