class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for i in range(len(ransomNote)):
            d[ransomNote[i]] += 1
        for j in range(len(magazine)):
            if magazine[j] in d and d[magazine[j]] > 0:
                d[magazine[j]] -= 1

        return True if sum(d.values()) == 0 else False
            
