class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Define result string and max length
        max_len = 1
        res_str = s[0]

        # Iterate through string
        for i in range(len(s)):
            cur_str = s[i]
            cur_len = 1
            for j in range(min(i, len(s) - 1 - i)): # Case for palindrome with 1 character center
                if s[i - j - 1] != s[i + j + 1]:
                    break
                cur_str = s[i - j - 1] + cur_str + s[i + j + 1]
                cur_len = cur_len + 2
            if cur_len > max_len:
                    max_len = cur_len
                    res_str = cur_str
            
            if (i < len(s) - 1) and (s[i] == s[i + 1]): # Case for palindrome with 2 character center
                cur_str = s[i] + s[i + 1]
                cur_len = 2
                for j in range(min(i, len(s) - i - 2)):
                    if s[i - j - 1] != s[i + j + 2]:
                        break
                    cur_str = s[i - j - 1] + cur_str + s[i + j + 2]
                    cur_len = cur_len + 2
                if cur_len > max_len:
                        max_len = cur_len
                        res_str = cur_str

        return res_str
    
# Testing
s = "cbbd"

test = Solution()
result = test.longestPalindrome(s)
print(result)