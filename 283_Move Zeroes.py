'''
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

# since first item may be 0, so start with left = -1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                if left == -1:
                    left = right
            else:
                if left != -1:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
        

        
