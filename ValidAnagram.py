from collections import defaultdict


class Solution:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
    def isAnagram1(self, s: str, t: str) -> bool: # Hash map solution
        # Base Case
        if len(s) != len(t): return False

        # Initialize hashmap
        hashmap = defaultdict(lambda : 0)

        # Iterate
        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        
        # Return
        return all(value == 0 for value in hashmap.values())
    
    def isAnagram2(self, s: str, t: str) -> bool: # sort solution
        # Base Case
        if len(s) != len(t): return False

        # Sort
        return ''.join(sorted(s)) == ''.join(sorted(t))

# Test Cases
solution = Solution()

s = "anagram"
t = "nagaram"

solution.isAnagram(s, t)
