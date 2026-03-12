class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                j = stack.pop()
                if stack:
                    h = min(height[stack[-1]],height[i]) - height[j]
                    w = i - stack[-1] - 1
                    water += h*w
            stack.append(i)
        return water
