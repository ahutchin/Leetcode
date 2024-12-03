from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # var def
        ptr1 = ptr2 = 0
        maxOnes = 0
        curOnes = 0
        elementDeleted = False

        # nums traversal
        while ptr2 < len(nums):
            if nums[ptr2] == 1:
                curOnes += 1
                ptr2 += 1
            else:
                if not elementDeleted:
                    elementDeleted = True
                    ptr2 += 1
                else:
                    while nums[ptr1] == 1:
                        ptr1 += 1
                        curOnes -= 1
                    ptr1 += 1
                    elementDeleted = False
            
            if curOnes > maxOnes:
                maxOnes = curOnes
        
        # return
        if not elementDeleted:
            return maxOnes - 1

        return maxOnes
    
# test
test = Solution()
result = test.longestSubarray([0,1,1,1,0,1,1,0,1])
print(result)

# Time Complexity: O(n) because we visit each node basically once
# Space Complexity: O(1) because we dont use substantial memory