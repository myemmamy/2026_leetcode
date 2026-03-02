class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        d = {}
        left,right = 0,0
        while right < len(s):
            if s[right] not in d:
                d[s[right]] = 1
            else:
                ans = max(ans,right-left)
                while s[right] in d:
                    d.pop(s[left])
                    left += 1
                d[s[right]] = 1
            right += 1
        return ans
