from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def DFS(root: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not root:
                return True
            elif root.val <= lower or root.val >= upper:
                return False
            else:
                return DFS(root.left, lower, root.val) and DFS(root.right, root.val, upper)
        
        return DFS(root, float('-inf'), float('inf'))
            

        # if not root.left and not root.right:
        #     return True
        # elif not root.left:
        #     if root.right.val > root.val:
        #         return self.isValidBST(root.right)
        #     else:
        #         return False
        # elif not root.right:
        #     if root.left.val < root.val:
        #         return self.isValidBST(root.left)
        #     else:
        #         return False
        # if root.left.val < root.val < root.right.val:
        #     return self.isValidBST(root.left) and self.isValidBST(root.right)
        # else:
        #     return False
        
        
# Doesnt handle this case: 
# root = [5,4,6,null,null,3,7]
# Output
# true
# Expected
# false


# Intuition:
# DFS while checking if children follow BST structure

# Time Complexity: O(n) we visit each node once
# Space Complexity: O(h) our recursion stack is height h