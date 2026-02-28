class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))
            elif len(tokens[i]) > 1 and tokens[i][0] == '-':
                stack.append(-int(tokens[i][1:]))
            elif tokens[i] in '+-*/':
                operand1 = stack.pop()
                operand2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(operand1+operand2)
                elif tokens[i] == '-':
                    stack.append(operand2-operand1)
                elif tokens[i] == '*':
                    stack.append(operand1*operand2)
                else:
                    stack.append(int(operand2/operand1))
        return stack[-1]


===========================================================
use lambda to simplify calculation
        operations = {
            '+': lambda x, y: x + y, 
            '*': lambda x, y: x * y, 
            '-': lambda x, y: x - y, 
            '/': lambda x, y: int(x / y)
        }

