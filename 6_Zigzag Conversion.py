class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        if numRows == 1:
            return s
        if numRows == 2:
            for i in range(len(s)):
                if i%2 == 0:
                    rows[0] += s[i]
                else:
                    rows[1] += s[i]
            return ''.join(rows)
        
        for i in range(len(s)):
            if i%(numRows-1) == 0 and i/(numRows-1)%2 == 0:
                rows[0] += s[i]
            elif i%(numRows-1) == 0 and i/(numRows-1)%2 !=0:
                rows[numRows-1] += s[i]
            elif i%(numRows-1) !=0 and i//(numRows-1)%2 == 0:
                rows[i%(numRows-1)] += s[i]
            else:
                rows[numRows-1-i%(numRows-1)] += s[i]
        return ''.join(rows)
