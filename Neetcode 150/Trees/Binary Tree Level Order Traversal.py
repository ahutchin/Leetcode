from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            curLevel = []
            for i in range(len(queue)):
                currNode = queue.popleft()
                curLevel.append(currNode.val)
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    
            res.append(curLevel)

        return res

# Intuition:
# BFS iterative implementation