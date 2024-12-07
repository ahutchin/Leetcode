from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # list.sort() uses the Timsort algorithm, which has a time complexity of O(n log n)
        nums.sort() # list.sort() modifies Lists in place
        return nums[-k]
    
    def findKthLargestHeap(self, nums: List[int], k: int) -> int: # O(n + n + klogn) ~ O(n) time complexity
        nums = [-x for x in nums] # flip elements of nums sign
        heapq.heapify(nums) # Turn nums into a heap in linear time
        # We are effectively making a max heap by multiplying nums by -1 because heapq.heapify creates min heaps
        for _ in range(k):
            res = heapq.heappop(nums)
        # return
        return res * -1

# test
test = Solution()
result = test.findKthLargest([3,2,1,5,6,4], 2)
print(result)