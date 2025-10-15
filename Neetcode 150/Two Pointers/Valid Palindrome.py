class Solution:
    def validPalindrome(self, s: str) -> bool:
        alphanumeric = 'abcdefghijklmnopqurstuvwxyz1234567890'
        s = s.lower().strip()

        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] not in alphanumeric or s[end] not in alphanumeric:
                if s[start] not in alphanumeric:
                    start += 1
                if s[end] not in alphanumeric:
                    end -= 1
            elif s[start] == s[end]:
                start += 1
                end -= 1
            elif s[start] != s[end]:
                return False
        
        return True


# Intuition:
# Strip of non alphanumeric characters, read from both ends

test = Solution()
word = "A man, a plan, a canal: Panama"
print(test.validPalindrome(word))