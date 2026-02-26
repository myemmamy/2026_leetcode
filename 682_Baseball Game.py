class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range(len(operations)):
            op = operations[i]
            if op[0] == '-' and op[1:].isdigit():
                score.append(int(op))
            elif op.isdigit():
                score.append(int(op))
            elif op == 'C':
                score.pop()
            elif op == 'D':
                score.append(2*score[-1])
            elif op == '+':
                r = score[-1] + score[-2]
                score.append(r)
        return sum(score)


            
