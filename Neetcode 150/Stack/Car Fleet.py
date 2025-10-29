from typing import List
import math
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Order cars by distance from target
        pairs = sorted(list(zip(position, speed)), reverse = True)

        # Calculate time it takes for each car to reach target and append to stack
        stack = deque()
        for pos, vel in pairs: 
            time = (target - pos) / vel
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
    
# Intuition:
# Order cars by distance from target - 0th index is closest to target
# Calculate the time it takes for the car to reach target
# Append time to monotonic stack starting from 0th index, if following index time is >= current car time, they form a fleet
position = [8,3,7,4,6,5]
speed = [4,4,4,4,4,4]
target = 10
sol = Solution()
print(sol.carFleet(target, position, speed))

# Time complexity: O(nlogn)
# Space complexity: O(n)