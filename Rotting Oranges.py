from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # var def
        rows = len(grid)
        columns = len(grid[0])
        rottenOranges = set()
        freshOranges = 0
        time = 0

        # bfs setup
        neighbors = set([(0, 1), (0, -1), (1, 0), (-1, 0)])
        queue, visited = collections.deque([]), set()

        # Find all rotten oranges
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rottenOranges.add((row, column))
                    visited.add((row, column))
                    queue.append((row, column))
                elif grid[row][column] == 1:
                    freshOranges += 1
        
        # if no oranges/only fresh oranges
        if freshOranges == 0:
            return 0
        elif len(rottenOranges) == 0:
            return -1
        
        # perform bfs
        while queue:
            for _ in range(len(queue)):
                curRow, curColumn = queue.popleft()

                for change_row, change_column in neighbors:
                    newRow =  curRow + change_row
                    newColumn = curColumn + change_column

                    if (0 <= newRow < rows) and (0 <= newColumn < columns) and (grid[newRow][newColumn] == 1) and ((newRow, newColumn) not in visited):
                        queue.append((newRow, newColumn))
                        visited.add((newRow, newColumn))
                        grid[newRow][newColumn] = 2
            time += 1
        
        # check if any non-rotten oranges exist
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    return -1
        
        # return
        return time - 1
                
# Locate rotting oranges
# Perform bfs on all of them simultaneously
# when all neighbors are 0 or 2 you need to return
# keep an active count going the whole time
# at the end check if any oranges are not rotten
# return count or -1

# Test
test = Solution()
result = test.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(result)

# Time Complexity: O(n * m) visit each orange like 4 or 5 times
# Space complexity: O(1) we dont use any more additional space