class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Find longer string
        longerString = max(len(s), len(t))
        sStack = []
        tStack = []

        # Iterate through the strings
        i = 0
        while i < longerString:
            if (len(s) > i):
                if (sStack) and (s[i] == '#'):
                    sStack.pop()
                elif (s[i] != '#'):
                    sStack.append(s[i])

            if (len(t) > i):
                if (tStack) and (t[i] == '#'):
                    tStack.pop()
                elif (t[i] != '#'):
                    tStack.append(t[i])

            i += 1
        
        # Return
        return sStack == tStack
    
# O(n) time complexity
# O(n + m) space complexity
    
# Test

solution = Solution()

s = "ab#c"
t = "ad#c"

result = solution.backspaceCompare(s, t)
print(result)