from typing import List

# Intuition: this very clearly feels like a Stack problem 
# Read through tokens and add each token to a Stack
# If the token in "-+/*", pop the two most recent integers and perform the operation on them, then add the outcome back to the stack
# Return stack.pop()

class Solution:
    # Time Complexity: O(n) because we read through tokens once
    # Space Complexity: O(n) worst case if all tokens are added to the stack
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "/*+-":
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    # Plus Case
                    stack.append(op1 + op2)
                elif token == "-":
                    # Minus Case
                    stack.append(op1 - op2)
                elif token == "*":
                    # Multiply Case
                    stack.append(op1 * op2)
                else:
                    # Divide Case
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack.pop()