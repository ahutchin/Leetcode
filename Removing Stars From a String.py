from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        # Define var
        stack = deque()
        
        # Read through stack
        for char in s:
            if (char != '*'):
                stack.append(char)
            elif (len(stack) > 0) and (char == '*'):
                stack.pop()
        
        # Return
        return "".join(stack)
            