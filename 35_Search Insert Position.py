
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        if target > nums[right]:
            return right + 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1
        return right

# above one right boundary = n-1, not cover n case, so need to use if to cover 
# another way is to use n
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1
        return right
