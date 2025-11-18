from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct Graph
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        res = []
        visited, cycle = set(), set()

        # DFS
        def DFS(course) -> bool:
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for prereq in graph[course]:
                if DFS(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if DFS(i) == False:
                return []
        return res
            
        

# Intuition:
# Create directed Graph
# Work backwards through the graph, adding each element to the results list
# Reverse the results list

# Time Complexity: O(E + V)
# Space Complexity: O(E + V)