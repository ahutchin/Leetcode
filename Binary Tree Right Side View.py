from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Case for empty root
        if root is None: 
            return []

        # var def
        result = []
        queue = deque([root])

        # bfs traversal
        while queue:
            lastNode = None

            for i in range(len(queue)):
                curNode = queue.popleft()
                if curNode.left is not None:
                    queue.append(curNode.left)
                if curNode.right is not None:
                    queue.append(curNode.right)
                lastNode = curNode

            result.append(lastNode.val)

        return result