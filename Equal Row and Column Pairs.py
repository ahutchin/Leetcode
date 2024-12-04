from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(n^2) solution
        # pair count
        count = 0

        # Add all rows to dictionary and track their occurences
        dict = defaultdict(int)
        for row in grid:
            dict[str(row)] += 1
        
        # Iterate through Columns and check if the same thing exist 
        for i in range(len(grid)):
            # build column
            column = []
            for row in grid:
                column.append(row[i])
            column = str(column)
            
            # check if column exists in dict
            if column in dict:
                count += dict[column]
        
        # return
        return count