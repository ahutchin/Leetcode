from typing import List, Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()

        def DFS(course: int) -> bool:
            if graph[course] == []:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for pre in graph[course]:
                if not DFS(pre):
                    return False
            
            graph[course] = []
            return True
        
        for c in range(numCourses):
            if not DFS(c):
                return False
        return True

# Intuition:
# To take course ai, we first need to take bi
# We can construct a directed graph
# If we detect a cycle in the graph, return false

# Time Complexity: O(V + E)
# Space Complexity: O(V)