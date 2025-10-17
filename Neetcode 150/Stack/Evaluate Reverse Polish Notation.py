from typing import List
from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        numbers = '1234567890'
        operations = '+-*/'

        for char in tokens:
            if char[-1] in numbers:
                stack.append(int(char))
            elif char[-1] in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                if char == '+':
                    stack.append(op1 + op2)
                elif char == '-':
                    stack.append(op1 - op2)
                elif char == '*':
                    stack.append(op1 * op2)
                elif char == '/':
                    stack.append(math.trunc(op1 / op2))
        
        return stack[0]

# Intuition
# if number, add to stack
# if operation, pop the 2 recent numbers, do the operation, add them back to stack

test = Solution()
res = test.evalRPN(["4","13","5","/","+"])
print(res)