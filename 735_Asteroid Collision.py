class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        for i in range(len(asteroids)):
            c =  asteroids[i]
            if not stack or c > 0 or (stack[-1] < 0 and c < 0):
                stack.append(c)
            elif stack[-1] > 0 and c < 0:
                active = True
                while stack and active and stack[-1] > 0:
                    if stack[-1] < abs(c):
                        stack.pop()
                    elif stack[-1] == abs(c):
                        stack.pop()
                        active = False
                        break
                    else:
                        active = False
                        break
                if active:
                    stack.append(c)

        return stack    
