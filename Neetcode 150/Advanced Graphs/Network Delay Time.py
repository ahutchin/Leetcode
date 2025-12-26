from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     # Construct Graph
    #     graph = defaultdict(lambda: [])
    #     for source, target, time in times:
    #         graph[source].append([target, time])

    #     # BFS
    #     counts = [-1] * (n + 1)
    #     counts[k], counts[0] = 0, 0
    #     queue = deque([[k, 0]])
    #     visited = set()
    #     while queue:
    #         node, sum = queue.popleft()
    #         for neighbor, cost in graph[node]:
    #             if counts[neighbor] == -1:
    #                 counts[neighbor] = sum + cost
    #             elif sum + cost < counts[neighbor]:
    #                 counts[neighbor] = sum + cost
    #             if neighbor not in visited:
    #                 queue.append([neighbor, sum + cost])
    #         visited.add(node)

    #     # return
    #     if min(counts) == -1:
    #         return -1
    #     else:
    #         return max(counts)

    # Dijkstra's
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Construct Graph
        graph = defaultdict(lambda: [])
        for source, target, time in times:
            graph[source].append([target, time])

        # Dijkstra's
        heap = [[0, k]]
        visited = set()
        t = 0

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            t = max(t, cost)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, [cost + weight, neighbor])

        return t if len(visited) == n else -1


# Intuition:
# Construct the graph
# BFS - to find the time it takes starting from node k to reach every other node
#     - store the minimum time it takes to reach each node
#     - when we reach the end of the graph, we return the minimum in the array

# Time Complexity: O(E + V)
# Space Complexity: O(Elog(V))


times = [[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46], [
    4, 1, 6], [5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58], [2, 4, 77], [5, 2, 74]]
n = 5
k = 3

Solution().networkDelayTime(times, n, k)
