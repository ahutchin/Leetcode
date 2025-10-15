from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        curChars = set()
        start = 0
        end = 0

        # Iterate
        count = 0
        while end < len(s):
            if s[end] not in curChars:
                curChars.add(s[end])
                count += 1
                end += 1
                if count > maxCount:
                    maxCount = count
            elif s[end] in curChars:
                while s[start] != s[end]:
                    curChars.remove(s[start])
                    start += 1
                    count -=1

                end += 1
                start += 1
        
        return maxCount

        
# Intuition:
# Store current longest substring in variable - curMax
# Use 2 pointers, shifting across s, storing the currently used chars in a set

test = Solution()
res = test.lengthOfLongestSubstring("")
print(res)