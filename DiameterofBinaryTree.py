from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        
        def dfs(root: Optional[TreeNode]) -> int:
            # Base Case
            if not root: return -1

            # Recursively call dfs on left and right nodes to get their heights
            left = dfs(root.left)
            right = dfs(root.right)

            # Compare current maxDiameter to newly calculated diameter
            maxDiameter[0] = max(maxDiameter[0], left + right + 2)

            # return
            return 1 + max(left, right)
        
        dfs(root)

        return maxDiameter[0]