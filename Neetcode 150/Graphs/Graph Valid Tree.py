from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(lambda: [])
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        visited = set()

        def DFS(node, prev) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not DFS(neighbor, node):
                    return False
            return True
        
        DFS(0, -1)
        return len(visited) == n
            

# Intuition:
# A valid tree is a connected graph with no cycles -- Should have n-1 edges

n=5
edges=[[0,1],[2,1],[3,2],[3,1],[4,1]]
print(Solution().validTree(n, edges))

# Time Complexity: O(E + V)
# Space Complexity: O(E + V) -- Graph