class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                if stack:
                    k = i-stack[-1]-1
                else:
                    k = i
                if nums[j] > threshold / k:
                    return k
            stack.append(i)
        return -1
