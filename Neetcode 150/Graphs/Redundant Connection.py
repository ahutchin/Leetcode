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
        parent = [i for i in range(len(edges) + 1)]
        def find(node) -> int:
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node, neighbor) -> None:
            root1 = find(node)
            root2 = find(neighbor)
            parent[root2] = root1

        for node, neighbor in edges:
            if find(node) == find(neighbor):
                return [node, neighbor]
            union(node, neighbor)


# Intuition:
# We construct the graph with the edge list
# The edge that turns the graph from valid to invalid is what we return

# Brute force:
# Everytime we add an edge, we check if theres a loop

# O(E) -> Add each neigbor, node pair to graph, if the node is alr in seen, then its invalid

print(Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))

# Time Complexity: O(E) - for every edge we do an O(1) operation (find, then union)
# Space Complexity: O(V) - we store every vertex and its parent