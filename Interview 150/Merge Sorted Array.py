from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p1 + p2 + 1] = nums1[p1]
                p1 -= 1
            else:
                nums1[p1 + p2 + 1] = nums2[p2]
                p2 -= 1
        
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


# Intuition:
# 2 pointers, append to nums1 from the end

# Time Complexity: O(n + m), we do a comparison operation for every index of nums1 & nums2
# Space Complexity: O(1), we don't take up any additional memory