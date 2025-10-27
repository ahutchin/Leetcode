from typing import List
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Recursively call '(' or ')' additions to existing stack
        res = []
        stack = deque([])

        # backtrack definition
        def backtrack(openParenthesisCount: int, closedParenthesisCount: int) -> None:
            if openParenthesisCount == closedParenthesisCount == n: # Base case (count of open and closed parenthesis equal to n)
                res.append(''.join(stack))
                return
        
            # Case for open parenthesis less than n
            if openParenthesisCount < n:
                stack.append('(')
                backtrack(openParenthesisCount + 1, closedParenthesisCount)
                stack.pop()
            
            # Case for closed parenthesis count less than open parenthesis count
            if closedParenthesisCount < openParenthesisCount:
                stack.append(')')
                backtrack(openParenthesisCount, closedParenthesisCount + 1)
                stack.pop()
            
            return
        
        backtrack(0, 0)
        return res

# Intuition:
# There is repeated work when making every parenthesis from start to finish
# Can I save on those operations?

# Time & Space complexity: O(4^n/sqrt(n)) time and O(n) space