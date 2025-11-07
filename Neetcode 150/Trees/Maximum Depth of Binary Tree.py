from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth = 0
        
        def DFS(root: Optional[TreeNode], currDepth: int) -> None:
            nonlocal depth
            depth = max(depth, currDepth)
            
            if root.left:
                DFS(root.left, currDepth + 1)
            if root.right:
                DFS(root.right, currDepth + 1)
            return
        
        DFS(root, 1)

        return depth
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Intuition:
# DFS, increment with each recursive call, remember current max