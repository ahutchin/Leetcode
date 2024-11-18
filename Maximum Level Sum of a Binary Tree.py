from typing import Optional
from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # var definition
        res = [0, float('-inf')]
        queue = deque([root])
        curLevel = 0

        # bfs traversal
        while queue:
            curSum = 0
            curLevel += 1

            for _ in range(len(queue)):
                curNode = queue.popleft()
                curSum += curNode.val
                if curNode.left is not None:
                    queue.append(curNode.left)
                if curNode.right is not None:
                    queue.append(curNode.right)
            
            if curSum > res[1]:
                res = [curLevel, curSum]

        # return
        return res[0]