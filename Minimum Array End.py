class Solution: # Time limit exceed (O(n) time)
    def minEnd1(self, n: int, x: int) -> int:
        out = [x]

        while len(out) < n:
            out.append((out[-1] + 1) | x)

        return out[-1]
    
    def minEnd2(self, n: int, x: int) -> int:
        result = x
        remaining = n - 1
        position = 1
    
        while remaining:
            if not (x & position):
                result |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
    
        return result

    
# Input: n = 3, x = 4
# Output: 6
# Explanation:
# nums can be [4,5,6] and its last element is 6.
# 100
# 101
# 110

# Input: n = 2, x = 7
# Output: 15
# Explanation:
# nums can be [7,15] and its last element is 15.
# 0111
# 1111

# Explination:
# I think the idea here is to start the output array with the target value x, 
# all subsequent numbers should share all 1 bits with x, but can have 1 bits where 
# x has 0 bits until the length of the array meets n

# TEST:
n = 2
x = 7
test = Solution()
result = test.minEnd1(n, x)