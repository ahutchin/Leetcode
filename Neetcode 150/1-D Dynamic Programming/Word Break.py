from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                t = len(word)
                if (i + t) <= len(s) and s[i:i + t] == word:
                    dp[i] = dp[i + t]
                if dp[i]:
                    break

        return dp[0]

# Intuition:
# Not sure how Dynamic Programming applies here

# IDEA: for word in dictionary if its present in s, remove it from s, iterate until we reach end of dictionary and return false, or until s is empty and return true
# Time complexity: O(m * n) where l is length of dict, and n is length of s
# This solution fails for the following situation: s = "cars", wordDict = ["car","ca","rs"]

# Alterntive: Recursive approach
# Explore the idea of removing each word in wordDict from the initial string s, and continueing after that removal
# Time Complexity: O(2^m * n)
# Fails for the following: s = "cbca", wordDict = ["bc","ca"]

# Alternative: Recursive approach without collapsing the string


s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))
