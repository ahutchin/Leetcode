class Solution:
    # Time Complexity: O(n) where n is the longer string, because perform a set number of operations for each char in a string of length n
    # Space Complexity: O(n) we take up additional space for the result string which will have a max length of n+1
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            aValue = ord(a[i]) - ord("0") if i < len(a) else 0 
            bValue = ord(b[i]) - ord("0") if i < len(b) else 0

            total = aValue + bValue + carry
            char = str(total % 2)
            result = char + result

            carry = total // 2

        if carry:
            result = "1" + result
        
        return result
    
# Test Case:
a = "11"
b = "1"

solution = Solution()

result = solution.addBinary(a,b)
print(result)