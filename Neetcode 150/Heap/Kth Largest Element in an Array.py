from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = [num * -1 for num in nums] # O(n)
        heapq.heapify(largest)
        for i in range(k): # O(k logn)
            res = heapq.heappop(largest)
        
        return res * -1

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort(reverse=True)
    #     return nums[k - 1]

# Intuition:
# non-heap: sort array in place (O(nlogn)) -> return k'th index
# heap: max heapify in place (O(n)) -> pop k times -> return final pop

nums = [3,2,1,5,6,4]
nums.sort(reverse=True)
print(nums)