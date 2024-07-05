class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        result = ""
        i = 0
        while i < len(s) and s[i] == " ": # Ignore leading whitespace
            i += 1

        # Check Sign of number
        if i < len(s):
            if s[i] not in "0123456789-+":
                return 0
            elif s[i] == '-':
                positive = False
                i += 1
            elif s[i] == '+':
                i += 1
            

        # Add each digit to result string
        while i < len(s) and s[i] in "0123456789":
            result += s[i]
            i += 1
        
        # Convert result into an integer
        if result == "":
            result += '0'
        result = int(result)

        # Convert result into correct sign
        if not positive:
            result *= -1
        
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648

        return result

# Test Case
solution = Solution()

s = "+1"

result = solution.myAtoi(s)
print(result)