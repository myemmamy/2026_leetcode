class Solution:
    def reverse(self, x: int) -> int:
        newx = 0
        maxV = 2 ** 31 -1
        minV = -(2 ** 31)
        y = abs(x)
        while y:
            n = y%10
            y = y//10
            newx = newx*10+n
            if x > 0 and newx > maxV:
                return 0
            elif x < 0 and -newx < minV:
                return 0
            
        return newx if x > 0 else -newx
