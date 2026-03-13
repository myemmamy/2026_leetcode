class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0
        def dfs(i,j):
            if i < 0 or i >= m or j <0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            c1 = dfs(i-1,j)
            c2 = dfs(i+1,j)
            c3 = dfs(i,j-1)
            c4 = dfs(i,j+1)
            return c1+c2+c3+c4+1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    new = dfs(i,j)
                    area = max(area,new)
        return area
            
