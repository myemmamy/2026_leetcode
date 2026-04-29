#recursion test
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(m):
            if m in memo:
                return memo[m]
            if m == 1:
                memo[1] = 1
                return 1
            if m == 2:
                memo[2] = 2
                return 2
            r1 = helper(m-1) + helper(m-2)
            memo[m] = r1
            return r1
        return helper(n)
#03182026, DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        if n < 2:
            return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-1]+dp[i-2])
        return dp[n]
