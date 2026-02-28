class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '*': lambda x,y: x*y,
            '/': lambda x,y: int(x/y),
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y
        }
        stack1,stack2 = [],[]
        n = 0
        for i in range(len(s)):
            if s[i].isdigit():
                n = n*10 + int(s[i])
            elif s[i] in '*/+-':
                if stack1 and stack1[-1][1] in '*/':
                    o1,op = stack1.pop()
                    r = operations[op](o1,n)
                    stack1.append((r,s[i]))
                else:
                    stack1.append((n,s[i]))
                n = 0
            else:
                pass
        o2 = n
        while stack1:
            o1,op = stack1.pop()
            if op in '+-':
                stack2.append((o2,op))
                o2 = o1
            else:
                o2 = operations[op](o1,o2)
        while stack2:
            o1,op = stack2.pop()
            o2 = operations[op](o2,o1)
        return o2
