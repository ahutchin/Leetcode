from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        # var definition
        provinceCount = 0
        visited = [False] * len(isConnected)
        index = 0

        # graph traversal
        while index < len(isConnected):
            if visited[index] == False:
                stack = deque([index])
                while (stack):
                    i = stack.pop()
                    for j in range(len(isConnected)):
                        if isConnected[i][j] == 1 and visited[j] == False:
                            stack.append(j)
                            visited[j] = True
                provinceCount += 1
            index += 1
        
        # return
        return provinceCount
    
    def findCircleNum2(self, isConnected: List[List[int]]) -> int: # More optimal of via better operations
        if not isConnected:
            return 0

        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == False:
                    visited[j] = True
                    dfs(j)

        for i in range(n):
            if visited[i] == False:
                count += 1
                visited[i] = True
                dfs(i)

        return count
        
        
# Time Complexity: O(n^2) because we visit each node once and do n check operations for it
# Space Complexity: O(n) because we use external memory to track visited nodes