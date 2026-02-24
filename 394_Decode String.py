class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num,substr='', ''
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num + s[i]
            elif s[i] == '[':
                stack.append((substr,int(num)))
                num = ''
                substr = ''
            elif s[i].isalpha():
                substr = substr + s[i]
            elif s[i] == ']':
                ss, n = stack.pop()
                substr = ss + n * substr
            i += 1
        
        return substr

