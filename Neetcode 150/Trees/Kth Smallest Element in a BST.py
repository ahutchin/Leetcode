from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def DFS(root: Optional[TreeNode]) -> None:
            nonlocal res

            if not root:
                return
            
            DFS(root.left)
            res.append(root.val)
            DFS(root.right)

        DFS(root)
        return res[k - 1]


# Intuition:
# Brute force -> Visit every node, return k'th smallest
# DFS, appending each node to a list, when the list's length equals k, return the last element of the list

# Time Complexity: O(n) we visit every node
# Space Complexity: O(h) our recursive stack is O(h)