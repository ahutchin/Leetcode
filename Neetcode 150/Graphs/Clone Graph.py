from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node: return None

        nodes = {}

        visited, q = set(), deque()
        q.append(node)

        # 1st pass
        while q:
            curr = q.popleft()

            if curr in visited:
                continue

            nodes[curr.val] = Node(curr.val)
            for neighbor in curr.neighbors:
                q.append(neighbor)
            visited.add(curr)

        # 2nd pass
        q.append(node)
        visited.clear()
        while q:
            curr = q.popleft()

            if curr in visited:
                continue

            for neighbor in curr.neighbors:
                nodes[curr.val].neighbors.append(nodes[neighbor.val])
                q.append(neighbor)
            visited.add(curr)
        
        return nodes[node.val]


# Intuition:
# Hashmap to store nodes at their index
# BFS:
# 2 pass:
# 1st pass: BFS on head -> We create a copy of the node -> continue on its neighbors

# Time Complexity: O(n + e) where e is edges
# Space Complexity: O(n) where n is number of nodes