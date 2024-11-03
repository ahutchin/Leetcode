class Solution:
    def rotateString(self, s: str, goal: str) -> bool: # Brute force
        # Var definition
        goalLen = len(goal)
        sLen = len(s)

        # Difference in lengths case
        if goalLen != sLen:
            return False

        # Read through goal string
        for i in range(goalLen):
            # Check if first character of s is equal to current character of goal
            j = 0
            if s[j] == goal[i]:
                while j < sLen:
                    j = j + 1
                    if j == sLen:
                        return True
                    if s[j] != goal[(i + j) % sLen]:
                        break
            
        return False
    
    def rotateString2(self, s: str, goal: str) -> bool:
        # Compare lengths
        if len(s) != len(goal): 
            return False
        
        # Make double string
        sDouble = s + s

        if goal not in sDouble:
            return False
        
        return True
        
# Testing
s = "abcde"
goal = "cdeab"

sol = Solution()
result = sol.rotateString(s, goal)
print(result)