class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            mid = (left + right) // 2
            rd = mid*(mid+1)//2
            if n < rd:
                right = mid - 1
            elif n == rd:
                return mid
            elif n > rd:
                left = mid + 1
        return left - 1
