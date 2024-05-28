#You are given a number string consists of digits, for example 1234. 
#Return a substring with the largest-valued odd integer or an empty string "" if no odd integer exists. eg 1234 should return 123. 
#
#part2: Given a binary string, rearrange the bits in the string to get a maximum odd number. 
#You can assume the string contains at least one '1'. 

class Solution:
    
    def findLargestBinary(self, s):
        #1111110001
        
        #for i in range(len(s)):
        #    if s[i] == 0: result += "0"
        #    elif s[i] == 1: result = "1" + result
        
        # if there are no '1's in the input string return ""
        if '1' not in s: return ""
        
        # sort the string
        s = sorted(s)
        
        # move the leftmost 1 to the right most position in the string
        s = s[1:] + "1"
        
        return s
    
    def findLargestOdd(self,s):
        # iterate through the string starting from the back
        length = len(s) - 1
        while length >= 0:
            if s[length] in "13579":
                return s[0:length + 1]
            length -= 1

        # return failure case
        return ""

#test case
testCase = Solution()

inputString = "1782166666222224444488888"

result = testCase.findLargestOdd(inputString)

inputString2 = "01010101010101010101010101"

result2 = testCase.findLargestBinary(inputString2)
print(result2)