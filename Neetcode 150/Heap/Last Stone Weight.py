from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, -(stone1 - stone2))
        
        return 0 if not heap else -heap[0]

# Intuition:
# Non-heap method: 
#   sort the arr (O(nlogn)) -> pit the 2 biggest boulders -> either both break, or the abs difference remains
#   insert the difference to the arr (O(logn))
# Heap method:
#   call heapify_max on stones -> pop 2 largest stones (O(logn)) -> heappush the difference (O(logn))

# Test
stones = [10,4,2,10]
print(Solution().lastStoneWeight(stones))

# Time Complexity: O(nlogn) we do a heappop for every element in stones
# Space Complexity: O(n) store in stones