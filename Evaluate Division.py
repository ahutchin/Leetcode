from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build adjacency list from equations & values
        adj = defaultdict(list)
        for index, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[index]])
            adj[b].append([a, 1 / values[index]])

        # Define dfs/bfs
        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1

            queue, visited = deque([]), set()
            queue.append([start, 1])
            visited.add(start)
            while queue:
                cur, w = queue.popleft()
                if cur == end:
                    return w
                
                for node, weight in adj[cur]:
                    if node not in visited:
                        visited.add(node)
                        queue.append([node, w * weight])
                
            return -1

        # Return result list from queries
        return [bfs(a, b) for a, b in queries]
    
# test
test = Solution()
result = test.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
print(result)

# Space complexity is O(n), Time complexity is also O(n)