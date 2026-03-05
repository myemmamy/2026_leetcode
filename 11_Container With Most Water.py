class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l,r = 0, len(height)-1
        while l < r:
            hl = height[l]
            hr = height[r]
            h = min(hl,hr)
            ans = max(ans,h*(r-l))
            if hl < hr:
                l += 1
            else:
                r -= 1
        return ans
