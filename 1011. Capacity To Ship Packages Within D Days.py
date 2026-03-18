class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = l + (r-l)//2
            if self.isValid(m,weights,days):
                r = m
            else:
                l = m + 1
        return l
    def isValid(self,x,weights,days):
        totaldays = 1
        w = 0
        for weight in weights:
            if w + weight <= x:
                w += weight
            else:
                totaldays += 1
                w = weight
        return totaldays <= days
