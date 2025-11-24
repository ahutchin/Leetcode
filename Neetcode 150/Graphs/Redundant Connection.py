from typing import List
from collections import defaultdict

class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     graph = defaultdict(lambda: [])
    #     visited = set()
    #     for neighbor, node in edges:
    #         if neighbor in visited and node in visited:
    #             return [neighbor, node]

    #         graph[node].append(neighbor)
    #         graph[neighbor].append(node)
    #         visited.add(node)
    #         visited.add(neighbor)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        


# Intuition:
# We construct the graph with the edge list
# The edge that turns the graph from valid to invalid is what we return

# Brute force:
# Everytime we add an edge, we check if theres a loop

# O(E) -> Add each neigbor, node pair to graph, if the node is alr in seen, then its invalid