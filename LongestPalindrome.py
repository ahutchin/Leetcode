from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initiate oddCounter and charMap
        oddCounter = 0
        charMap = defaultdict(lambda : 0)

        # Iterate
        for i in s:
            charMap[i] += 1
            if charMap[i] % 2 == 1:
                oddCounter += 1
            else:
                oddCounter -= 1
        
        # Return
        return len(s) - oddCounter + 1 if oddCounter > 1 else len(s)
    
# Test Case
solution = Solution()

s = "abccccdd"

result = solution.longestPalindrome(s)
print(result)