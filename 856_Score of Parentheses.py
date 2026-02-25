class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = [0]
        dep = -1
        for i in range(len(s)):
            if s[i] == '(':
                score.append(0)
            else:
                prev = score.pop()
                v = 1 if prev == 0 else 2 * prev
                score[-1] += v
        return score[0]
