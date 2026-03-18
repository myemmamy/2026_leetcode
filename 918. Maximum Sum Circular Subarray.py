class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ansmax,ansmin = nums[0],nums[0]
        curmax = nums[0]
        curmin = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            curmax = max(nums[i],curmax+nums[i])
            curmin = min(nums[i],curmin+nums[i])
            total += nums[i]
            ansmax = max(curmax,ansmax)
            ansmin = min(curmin,ansmin)
        if ansmax < 0:
            return ansmax
        else:
            return max(ansmax, total - ansmin)
