class Solution:
    # Space Complexity: O(1)
    # Time Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        # Initialize Alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"

        # Set to lowercase
        s = s.lower()

        # 2 pointers
        i, j = 0, len(s) - 1

        # Iterate from either end
        while i <= j:
            if s[i] not in alphabet or s[j] not in alphabet:
                if s[i] not in alphabet:
                    i += 1
                if s[j] not in alphabet:
                    j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                return False
        
        # Return
        return True
    
# Test Case
solution = Solution()

s = "0P"

result = solution.isPalindrome(s)
print(result)