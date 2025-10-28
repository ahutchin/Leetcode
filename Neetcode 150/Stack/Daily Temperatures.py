from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for i, currentTemp in enumerate(temperatures): 
            while stack and currentTemp > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res



# Intuition
# Brute force: O(n^2) time by going one index at a time and traversing until we find a temp greater than that index
# Issue here is that we are repeating work when we traverse forward then go back to repeat the process with the next index
# Monotonic Stack ?
# Check current temp with top of stack, if current temp > top of stack, pop the top of stack and set the value of that index in the result array, 
# continue until either the stack is empty or the top of the stack is greater than the current temp
# append current temperature, index to stack

# Time & Space Complexity: Time is O(n), Space is O(n)