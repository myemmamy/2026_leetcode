class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ansmax = nums[0]
        curmax,curmin = nums[0],nums[0]
        for i in range(1,len(nums)):
            a = curmax*nums[i]
            b = curmin*nums[i]
            if nums[i] >= 0:
                curmax = max(nums[i],a)
                curmin = min(nums[i],b)
            else:
                curmax = max(nums[i],b)
                curmin = min(nums[i],a)
            ansmax = max(ansmax,curmax)
        return ansmax
