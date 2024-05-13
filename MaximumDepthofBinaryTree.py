from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n) because we visit each node
    # Space Complexity: O(h) where h is the height of the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case:
        if not root: return 0

        # Recursively call maxDepth on the left and right nodes
        leftNode = self.maxDepth(root.left)
        rightNode = self.maxDepth(root.right)

        # Return
        return 1 + max(leftNode, rightNode)