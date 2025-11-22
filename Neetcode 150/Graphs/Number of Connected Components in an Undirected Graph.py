from typing import List
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Construct Undirected Graph
        graph = defaultdict(lambda: [])
        for node, neighbor in edges: # O(E)
            graph[node].append(neighbor)
            graph[neighbor].append(node)

        # DFS definition
        visited = set()
        components = 0
        def DFS(node) -> None: # O(V)
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                DFS(neighbor)

        
        for node in graph: # O(V)
            if node not in visited:
                DFS(node)
                components += 1
        
            return components + (n - len(visited))
        



# Intuition:
# Construct undirected graph - TC: O(E), SC: O(V + E)
# BFS through each node, using hash set to mark visited nodes, incrementing Connected Component Count
# If visited < n, increase Connected Component Count by the difference

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)