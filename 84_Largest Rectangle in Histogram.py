class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                new = heights[j] * w
                area = max(area, new)
            stack.append(i)
        return area
