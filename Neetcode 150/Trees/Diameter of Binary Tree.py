from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def DFS(root: Optional[TreeNode]) -> None:
            nonlocal depth

            if not root:
                return 0
            
            leftHeight = DFS(root.left)
            rightHeight = DFS(root.right)
            depth = max(depth, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        DFS(root)
        return depth

# Intuition:
# Base Case - Leaf node

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
