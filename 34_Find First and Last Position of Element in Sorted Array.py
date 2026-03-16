class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        l,r = 0,len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        if l <= len(nums)-1 and nums[l] == target:
            ans[0] = l

        l,r = 0,len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        if r > 0 and nums[r-1] == target:
            ans[1] = r-1
        return ans
