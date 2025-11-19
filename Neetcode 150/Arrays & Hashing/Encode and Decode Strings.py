from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        nums = "1234567890"

        res = []
        i = 0
        while i < len(s):
            currNum = ""
            while s[i] in nums:
                currNum += s[i]
                i += 1
            i += 1
            stopIndex = i + int(currNum)
            currWord = ""
            while i < stopIndex:
                currWord += s[i]
                i += 1
            res.append(currWord)
        return res


# Intuition:
# Use delimiter and string length to tell decoder how many of the following characters are 

# Time Complexity: O(n) for decode & encode
# Space Complexity: O(n) we use space equal to the input strings