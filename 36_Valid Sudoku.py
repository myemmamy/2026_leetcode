class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        from collections import defaultdict
        bh = [defaultdict() for i in range(n)]
        bv = [defaultdict() for i in range(n)]
        b = [defaultdict() for i in range(n)]
        for i in range(len(board)):
            for j in range(len(board)):
                c = board[i][j]
                if c == '.':
                    continue
                if c in bh[i]:
                    return False
                if c in bv[j]:
                    return False
                v = (i//3)*3+(j//3)
                if c in b[v]:
                    return False
                bh[i][c] = 1
                bv[j][c] = 1
                b[v][c] = 1
        return True
