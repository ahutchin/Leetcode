from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Time Complexity: 0(n) because each tree node is only visited once
    # Space Complexity: O(h) for the height of the tree 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]):
            # Base Case
            if not root: return [True, 0]

            # Recursively call dfs on left and right node
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

            # Return
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]