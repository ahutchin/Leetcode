from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
    
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(currNode.val)  # currNode is the last node in this level
    
        return res            

# Intuition:
# BFS -> only add last node in level to output List
# Time Complexity: O(n) because we visit each node 1 time, and do a constant number of operations
# Space Complexity: O(w) where w is the longest level