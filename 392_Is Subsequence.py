class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i,j=0,0
        while i < len(s) and j < len(t):
            ss = s[i]
            tt = t[j]
            if ss == tt:
                if i == len(s)-1:
                    return True
                i += 1
                j += 1
            else:
                j += 1
        return False
