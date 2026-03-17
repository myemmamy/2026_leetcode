class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l+1 < r:
            m = (l+r) // 2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            elif nums[m-1] < nums[m]:
                l = m
            else:
                r = m
        if nums[l] > nums[r]:
            return l
        else:
            return r
