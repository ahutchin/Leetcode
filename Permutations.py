from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Base Case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result
    
# Test Case
nums = [1,2,3]

solution = Solution()

result = solution.permute(nums)