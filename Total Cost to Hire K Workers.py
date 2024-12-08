from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int: # O(n) avg time, O(nlogn) worst case when k = n
        # setup
        totalCost = 0
        if candidates >= len(costs) / 2:
            minHeap = [(cost, index) for index, cost in enumerate(costs)] # O(n)
            heapq.heapify(minHeap) # O(n)
            costs = []
        else:
            minHeap = [(cost, index) for index, cost in enumerate(costs[:candidates])] + [(cost, index) for index, cost in enumerate(costs[-candidates:], start=len(costs) - candidates)] # O(2k)
            heapq.heapify(minHeap) # O(2k)
            costs = costs[candidates:-candidates]
        
        # Iteration
        for _ in range(k): # O(k) where k is the number of candidates
            # pop lowest cost candidate
            cost, index = heapq.heappop(minHeap) # O(logn) time
            totalCost += cost
            # Add to minHeap if candidates are still present in costs
            if len(costs) > 0:
                if index < candidates:
                    heapq.heappush(minHeap, (costs.pop(0), index))
                else:
                    heapq.heappush(minHeap, (costs.pop(), index))
        
        # return
        return totalCost
    
# Test
test = Solution()
result = test.totalCost([10,1,11,10], 2, 1)
print(result)

# i cant believe how slow this is compared to the other lc solutions :sob: I felt like this was such a solid answer
# Time Complexity: worst case nlogn
# Space complexity: n, cause we use 1 heap