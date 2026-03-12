class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for j in range(n):
                if row[j] != "0":
                    heights[j] += 1
                else:
                    heights[j] = 0
            a = self.getLargestRectangle(heights)
            ans = max(ans,a)
            print(a)
        return ans
        
    def getLargestRectangle(self,heights):
        heights.append(0)
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                new = heights[j] * w
                area = max(area,new)
            stack.append(i)
        return area
