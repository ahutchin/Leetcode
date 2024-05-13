from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if root == None: return None
        
        # We want to perform the following operations:
        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        # Recursively call invertTree on the children nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return
        return root