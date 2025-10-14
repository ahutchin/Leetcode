class Solution:
    def numTilings(self, n: int) -> int:
        

# Theres probably a mathematical pattern to this problem as n grows
# n     output
# 1     1
# 2     2
# 3     5
# 4     9   ==, ||||, |=|, ||=, =||, |<>, <>|, <->, <->

# Alternatively, maybe we track the count some how as moving from left to right of the 2xn grid 