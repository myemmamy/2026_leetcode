class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        for i in range(len(asteroids)):
            tag = 0
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                if not stack:
                    stack.append(asteroids[i])
                    continue
                if stack[-1] < 0:
                    stack.append(asteroids[i])
                elif 0 < stack[-1] < abs(asteroids[i]): 
                    while stack:
                        if stack[-1] < 0:
                            break
                        if stack[-1] < abs(asteroids[i]):
                            stack.pop()
                        elif stack[-1] == abs(asteroids[i]):
                            stack.pop()
                            tag = 1
                            break
                        else:
                            tag = 1
                            break
                    if not tag :
                        stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif stack[-1] > abs(asteroids[i]):
                    pass
        return stack
                    
                
                    
