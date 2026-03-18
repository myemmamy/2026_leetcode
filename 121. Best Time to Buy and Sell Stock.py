class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            minv = min(minv,prices[i])
            ans = max(ans, prices[i]-minv)
        return ans
