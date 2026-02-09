'''
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def getPalindrome(self,s,l,r):
        while r < len(s) and l >= 0 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    def longestPalindrome(self, s: str) -> str:
        sub = s[0]
        for i in range(len(s)-1):
            newsub1 = self.getPalindrome(s,i,i)
            newsub2 = self.getPalindrome(s,i,i+1)
            longsub = newsub2 if len(newsub2) > len(newsub1) else newsub1
            if len(longsub) > len(sub):
                sub = longsub
        return sub
