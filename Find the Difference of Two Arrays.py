from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1 - nums2), list(nums2 - nums1)]

# Test
test = Solution()
result = test.findDifference([1,2,3], [2,4,6])

# O(n + m) time & space complexity