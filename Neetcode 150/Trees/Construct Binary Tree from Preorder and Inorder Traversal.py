from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # O(n^2) time due to .index()
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
     
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # using array to track indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            mid = inorder_map[preorder[self.pre_idx]]
            self.pre_idx += 1
            
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
        
        return helper(0, len(inorder) - 1)
# Intuition:
# preorder array's first index is always the root of the current Tree
# the root's value in the inorder list determines how many following values in the preorder array are for left vs right subtree

# O(n) time 
# O(n) space