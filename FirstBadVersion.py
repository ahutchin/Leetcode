# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Intuition, this is an implementation of binary search
        low = 1
        high = n

        # Iterate
        while (low < high):
            mid = low + (high - low) // 2
            if (isBadVersion(mid)):
                high = mid
            else:
                low = mid + 1

        # Return
        return low