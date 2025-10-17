from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        chars = '([{'
        complements = ')]}'
        complementsDict = {')': '(', ']':'[', '}': '{'}

        for char in s:
            if char in chars:
                stack.append(char)
            elif char in complements:
                if not stack: # Case for complement character but empty stack
                    return False
                elif stack[-1] != complementsDict[char]: # Case for current char is complement and does not match top of stack
                    return False
                elif stack[-1] == complementsDict[char]: # Case for current char is complement and matches top of stack
                    stack.pop()
        
        if stack: # Case for stack is not empty
            return False

        return True
                

            


# Intuition:
# Use python stack data structure
# traverse string from left to right, 
#   when running into '([{', add that char to stack 
#   when running into ')]}', 
#       check if it's complement is on top of the stack, 
#           if so pop the complement
#           if not return false
# STACK MUST BE EMPTY BY END OF TRAVERSAL