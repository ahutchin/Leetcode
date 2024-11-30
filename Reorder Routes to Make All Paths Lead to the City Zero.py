from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # var definition
        roads = { (a, b) for a, b in connections } # Idea here is to first add all edges to a set, so we can search and access them in O(1) time
        neighbors = { city: [] for city in range(n) } # Then we have a set that contains dictionaries of each node where we can track its neighbors
        visited = set()
        changes = 0

        # Update neighbors
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # dfs
        def dfs(city: int): # goal here is to look at current city's neighbors, check direction of road, and increment changes accordingly
            nonlocal roads, neighbors, visited, changes

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in roads:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        
        visited.add(0)
        dfs(0)

        # return
        return changes

# Test
test = Solution()
result = test.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
print(result)

# O(n) time due to visiting each node a finite number of times
# O(n) space for the same reason