'''
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        for d in s1:
            need[d] = need.get(d,0) + 1
        print(f'need: {need}')
        k = len(s1)
        window = {}
        left = 0
        right = 0
        win = {}
        while right < len(s2) and len(win) < k:
            c = s2[right]
            if c not in need:
                left = right + 1
                win = {}
            else:
                win[c] = win.get(c,0) + 1
                if win == need:
                    return True
                while win[c] > need[c]:
                    cc = s2[left]
                    win[cc] -= 1
                    left += 1            
            right += 1 
        return False     
