# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int: 
        # var def
        upper = n
        lower = 1
        num = (upper - lower + 1) // 2
        res = guess(num)

        while res != 0:
            if res == 1:
                lower = num + 1
                upper = upper
                num = lower + (upper - lower + 1) // 2
            else:
                lower = lower
                upper = num - 1
                num = lower + (upper - lower + 1) // 2
            res = guess(num)

        return num
    
    def guessNumberv2(self, n: int) -> int: # GPT revised version
        lower = 1
        upper = n

        while lower <= upper:
            num = (upper + lower) // 2
            res = guess(num)
            if res == 0:
                return num
            elif res == 1:
                lower = num + 1
            else:
                upper = num - 1

        return -1
    
# Time Complexity: O(logn)
# Space Complexity: O(1)