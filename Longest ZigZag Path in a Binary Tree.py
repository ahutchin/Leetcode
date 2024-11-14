from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dfs algorithm
        def dfs(node: Optional[TreeNode], depth: int, isLeft: bool) -> int:
            # base case
            if node is None:
                return depth
            
            # logic for left-right traversal
            if isLeft:
                depth = max(dfs(node.right, depth + 1, False), dfs(node.left, 0, True))
            else:
                depth = max(dfs(node.left, depth + 1, True), dfs(node.right, 0, False))

            return depth

        # dfs call
        return max(dfs(root.left, 0, True), dfs(root.right, 0, False))