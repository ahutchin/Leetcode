from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: # Version 1
        # var definition
        roomsBool = [False] * len(rooms)
        roomsBool[0] = True

        queue = deque([rooms[0]])

        # Read through graph
        while queue:
            curRoom = queue.pop()
            for num in curRoom:
                if roomsBool[num] is False:
                    queue.append(rooms[num])
                    roomsBool[num] = True
                
        # return
        for el in roomsBool:
            if el is False:
                return False
        return True

        
# Initial Thoughts:
# Read through the Graph, visiting every available node, and tracking which rooms are open
# Utilize recursion

# Test
testcase = Solution()
result = testcase.canVisitAllRooms([[1],[2],[3],[]])
print(result)

# Time Complexity: O(n + k) only visit each room one time and do an operation for every key
# Space Complexity: O(n) we use an array of length n to store key info