time: O(m+n), space: O(m+n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a1,a2 = [],[]
        for c1 in s:
            if c1 != '#':
                a1.append(c1)
            else:
                if a1:
                    a1.pop()
        for c2 in t:
            if c2 != '#':
                a2.append(c2)
            else:
                if a2:
                    a2.pop()
        return a1 == a2
============================================================
time: O(m+n), space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i,j = len(s)-1,len(t)-1
        skip1, skip2 = 0,0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skip1 += 1
                    i -=1
                elif skip1 > 0:
                    skip1 -= 1
                    i -=1
                else:
                    break
            while j >=0:
                if t[j] == '#':
                    skip2 += 1
                    j -= 1
                elif skip2 > 0:
                    skip2 -=1 
                    j -= 1
                else:
                    break
            if i >=0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
