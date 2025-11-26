class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n): # Odd lengthed palindromes
            count += 1
            l, r = i - 1, i + 1
            while (l >= 0 and r <= n - 1 and
                s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
        
        for i in range(n - 1): # Even lengthed palindromes
            l, r = i, i + 1
            while (l >= 0 and r <= n - 1 and
                s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
        
        return count
# Intuition:
# Reminds me of Palindrom Partition
# Not too sure how DP plays a role in this problem

# Implementation is same as Longest Palindromic Substring

# Time Complexity: O(n^2) - we do n operations for each char in s
# Space Complexity: O(1) - we do not use any notable amount of additional memory