from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case
        if len(s) != len(t): return False

        # define dict
        letters = defaultdict(lambda: 0)

        # Start indexing
        for index in range(len(s)):
            letters[s[index]] += 1
            letters[t[index]] -= 1

        # check for non-zero value in letters
        for key in letters:
            if letters[key] != 0:
                return False
        
        return True

# Initial Thought:
# Count number of each character for s & t
# Compare if they match
# Use a single defaultdict(int), and if there is any values other than zero, return false

# Solution:
# O(n) time O(n) space, where n is the length of the s