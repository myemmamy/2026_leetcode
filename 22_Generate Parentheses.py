class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l,r = 0,0
        ans = []
        s = ''
        def helper(l,r,s):
            if l > n or r > l:
                return
            if len(s) == n*2:
                ans.append(s)
                return
            if l < n:
                helper(l+1,r,s+'(')
            if r < l:
                helper(l,r+1,s+')')
        helper(0,0,'')
        return ans
