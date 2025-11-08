from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def DFS(root: Optional[TreeNode]) -> int:
            nonlocal balanced

            if not root:
                return 0
            
            leftHeight = DFS(root.left)
            rightHeight = DFS(root.right)

            if abs(leftHeight - rightHeight) > 1: 
                balanced = False

            return 1 + max(leftHeight, rightHeight)
        
        DFS(root)
        return balanced

# Intuition:
# Recursive DFS -> pass the max number of edges up, 
# if edges on left ever exceed right by more than 1, return False

# Time Complexity: O(n)
# Space Complexity: O(h)