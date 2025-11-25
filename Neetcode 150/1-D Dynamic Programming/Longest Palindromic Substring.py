class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength, res = 1, s[0]
        n = len(s)
        for i in range(n): # Odd lengthed palindrome
            l, r = i - 1, i + 1
            length = 1
            while (l >=0 and r <= n - 1 and
                   s[l] == s[r]):
                length += 2
                l -= 1
                r += 1
            if length > maxLength:
                maxLength = length
                res = s[l+1:r]

        for i in range(n - 1): # Even lengthed palindrome
            l, r = i, i + 1
            length = 0
            while (l >= 0 and r <= n - 1 and 
                   s[l] == s[r]):
                length += 2
                l -= 1
                r += 1
            if length > maxLength:
                maxLength = length
                res = s[l+1:r]
        
        return res

# Intuition:
# Treat each char in s as the center of the palindrome, expand outward

Solution().longestPalindrome("babad")

# Time Complexity: O(n^2)
# Space Complexity: O(1)