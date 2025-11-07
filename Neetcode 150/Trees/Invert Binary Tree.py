from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.left == None and root.right == None:
            return root
        
        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root
        
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = deque([root])

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root


# Intuition:
# O(n) time - visit each node once & swap its children
# O(n) space - recursion stack