class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        nums.append(0)
        n = len(nums)
        ans = 0
        presum = [0]*n
        for i in range(1,n):
            presum[i] = presum[i-1] + nums[i-1]
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                j = stack.pop()
                if stack:
                    v = nums[j] * (presum[i] - presum[stack[-1]+1]) #sum(nums[stack[-1]+1:i])
                else:
                    v = nums[j] * presum[i] #sum(nums[:i])
                ans = max(ans,v)    
            stack.append(i)
        return ans%MOD
