class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Var definition
        maxVow = 0
        vowCount = 0
        left = 0
        right = k

        # Count vowels in first substring of length k
        for i in range(k):
            if s[i] in "aeiou":
                vowCount = vowCount + 1
        if vowCount > maxVow:
                maxVow = vowCount

        # Sliding window for checking remainder of s
        while right < len(s):
            if s[left] in "aeiou":
                vowCount = vowCount - 1
            if s[right] in "aeiou":
                vowCount = vowCount + 1
            
            if vowCount > maxVow:
                maxVow = vowCount
            
            left = left + 1
            right = right + 1
        
        # return
        return maxVow
