from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        labels = Counter(tasks)
        maxHeap = [-cnt for cnt in labels.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        while q or maxHeap:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


# Intuition:
# Count Tasks -- Maximum number of different labels is 26 (one for each letter), we can store the count of each label in a hashtable
#   first label should be the one with the most tasks
# Use a heap to store the tasks witht the largest count
# Use a queue to cooldown the processed tasks

# Time complexity: O(n) where n is number of tasks
# Space comlpexity: O(n)