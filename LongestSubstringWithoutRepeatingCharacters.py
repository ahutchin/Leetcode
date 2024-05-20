# Intuition: This feels like an adaptation of Kadane's Algorithm
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left, right = 0, 0
        maxLength = 0

        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
            else:
                chars.remove(s[left])
                left += 1
            
            maxLength = max(maxLength, right - left)

        return maxLength
    
# Test Case
s = "abcabcbb"

solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)