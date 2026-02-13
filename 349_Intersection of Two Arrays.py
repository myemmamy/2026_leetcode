class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums1,nums2 = (nums2,nums1) if len(nums2) > len(nums1) else (nums1,nums2)
        res = []
        oldt,left = -1, -1
        for i in range(len(nums2)):
            t = nums2[i]
            if t == oldt:
                continue
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] == t:
                    res.append(t)
                    oldt = t
                    break
                elif nums1[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
        return res
