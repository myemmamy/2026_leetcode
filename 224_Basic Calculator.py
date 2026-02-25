class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in '+-':
                res += num * sign
                num = 0
                if s[i] == '+':
                    sign = 1
                else:
                    sign = -1
            elif s[i] == '(':
                stack.append((res,sign))
                res,sign = 0,1
            elif s[i] == ')':
                res += num*sign
                preres, prevsign = stack.pop()
                res = preres + prevsign * res
                num = 0
            else:
                pass
        return res + num * sign
            
