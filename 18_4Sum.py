'''
Medium
Topics
premium lock icon
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''


#20260209
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        s = set()
        for i in range(len(nums)-4 + 1):
            a1 = nums[i]
            for j in range(i+1,len(nums)-3+1):
                a2 = nums[j]
                sum = target - a1 - a2
                left, right = j + 1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        if (nums[i],nums[j],nums[left], nums[right]) not in s:
                            res.append([nums[i],nums[j],nums[left], nums[right]])
                            s.add((nums[i],nums[j],nums[left], nums[right]))
                        left += 1
                    elif nums[left] + nums[right] < sum:
                        left += 1
                    else:
                        right -= 1
        return res

#20260210 change way to detect dup
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                t1 = nums[i] + nums[j] 
                t2 = target - t1
                left = j+1
                right = len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == t2:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] < t2:
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1                        
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1                   
        return res
            
