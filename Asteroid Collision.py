from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Base case
        if len(asteroids) == 0:
            return []
        
        # var def
        asteroids = deque(asteroids)
        stack = deque([])

        # traverse asteroids
        while (asteroids):
            asteroid = asteroids.popleft()
            if asteroid > 0 or len(stack) == 0:
                stack.append(asteroid)
            else:
                while (len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroid)):
                    stack.pop()
                if (len(stack) > 0 and stack[-1] == abs(asteroid)):
                    stack.pop()
                elif (len(stack) == 0 or stack[-1] < 0):
                    stack.append(asteroid)
        
        return list(stack)
    
# Testcase
test = Solution()
result = test.asteroidCollision([5,10,-5])
print(result)