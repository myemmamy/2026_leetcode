class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        seen = set()
        m = len(s)
        n = len(t)
        if m != n:
            return False
        for i in range(n):
            if t[i] not in seen and s[i] not in d:
                seen.add(t[i])
                d[s[i]] = t[i]
            elif t[i] in seen and s[i] not in d:
                return False
            elif t[i] not in seen and s[i] in d:
                return False
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
