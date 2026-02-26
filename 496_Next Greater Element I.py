class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        #res2 = [-1] * n
        d2 = {}
        stack = []
        res1 = []
        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                p = stack.pop()
                #res2[p] = i 
                d2[nums2[p]] = nums2[i]
            stack.append(i)
        for j in range(m):
            res1.append(d2.get(nums1[j],-1))
        return res1
