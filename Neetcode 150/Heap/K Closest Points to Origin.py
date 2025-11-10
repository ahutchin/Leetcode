from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate distance:
        distances = []
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            distances.append((distance, i))
        heapq.heapify(distances)

        res = []
        for i in range(k):
            min = heapq.heappop(distances)
            res.append(points[min[1]])
        
        return res

# Intuition:
# non-heap -> calculate each point's distance from origin (O(n)) and add (distance, index) to list -> Sort (O(nlogn)) -> Return first k indices
# heap -> min heap, heapify points (O(n)) (distance, index) -> pop k elements (O(klog(n)))

# Time complexity: 