class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        arr.append(0)
        MOD = 10**9 + 7
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                if stack:
                    w = (i-j)*(j-stack[-1])
                else:
                    w = (i-j)*(j+1)
                ans += arr[j] * w
            stack.append(i)
        return ans%MOD
