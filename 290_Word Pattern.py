class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        m = len(pattern)
        n = len(slist)
        if m!=n:
            return False
        d = {}
        seen = set()
        for i in range(n):
            print(d)
            print(seen)
            if pattern[i] not in d and slist[i] not in seen:
                d[pattern[i]] = slist[i]
                seen.add(slist[i])
            elif pattern[i] in d and d[pattern[i]] != slist[i]:
                return False
            elif pattern[i] not in d and slist[i] in seen:
                return False
            elif pattern[i] in d and slist[i] not in seen:
                return False
            else:
                if d[pattern[i]] != slist[i]:
                    return False
        return True
