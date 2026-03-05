class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        ans = float('inf')
        total = 0
        while r < len(nums):
            if nums[r] == target:
                return 1
            total += nums[r]
            while total >= target:
                ans = min(ans,r-l+1)
                total -= nums[l]
                l += 1
                if total < target:
                    break
            r +=1
        return 0 if ans == float('inf') else ans
