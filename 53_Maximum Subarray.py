class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        presum = [0] * (n+1)
        presum_min = [0] * (n+1)
        max_sum = -float('inf')
        for i in range(1,len(nums)+1):
            presum[i] = presum[i-1]+nums[i-1]
            presum_min[i] = min(presum_min[i-1],presum[i])
            max_sum = max(max_sum, presum[i] - presum_min[i-1])
        return max_sum
