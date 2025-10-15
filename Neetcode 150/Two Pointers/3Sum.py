from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # Iterate
        for i in range(len(nums)):
            # Check for repeat:
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            start = i + 1
            stop = len(nums) - 1
            while start < stop:
                if nums[start] + nums[stop] == target:
                    result.append([nums[i], nums[start], nums[stop]])
                    start += 1
                    stop -= 1
                    while start < stop and nums[start] == nums[start - 1]:
                        start += 1
                    while start < stop and nums[stop] == nums[stop + 1]:
                        stop -= 1
                elif nums[start] + nums[stop] < target:
                    start += 1
                elif nums[start] + nums[stop] > target:
                    stop -= 1
            
        return result
# Intuition:
# use a set to store triples to prevent repeated results

# Optimal Sol:
# we have a set for the first num, then use two pointer on nums sorted to find the remaining 2 numbers,

test = Solution()
result = test.threeSum([0,0,0])
print(result)