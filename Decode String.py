from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        stack = deque([""])
        
        # traverse stack
        for char in s:
            if char.isdigit():
                if len(stack[-1]) > 0 and stack[-1].isdigit():
                    stack[-1] += char
                else:
                    stack.append(char)
            elif char == '[':
                stack.append("")
            elif char == ']':
                chars = stack.pop()
                count = int(stack.pop())
                stack[-1] += (chars * count)
            else:
                stack[-1] += char
        
        # return
        return stack[0]

# Test
test = Solution()
result = test.decodeString("100[leetcode]")
print(result)

# Time Complexity: O(n) because we visit each element in the input string once
# Space Complexity: O(n) because we use a stack to store the input string