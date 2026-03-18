class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        tmin = 1
        tmax = max(piles)
        while tmin < tmax:
            m = tmin + (tmax-tmin) // 2
            if self.isValid(m,piles,h):
                tmax = m
            else:
                tmin = m + 1
        return tmin

    def isValid(self,x,piles,h):
        total = 0
        for pile in piles:
            t = (pile + x - 1)//x
            total += t
        return total <= h
