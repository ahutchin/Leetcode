from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # dfs definition
        def dfs(curNode: Optional[TreeNode], leafSequence: List[int]) -> None:
            # Base Case
            if curNode is None: 
                return
            
            # Leaf node check
            if (curNode.left is None) and (curNode.right is None):
                leafSequence.append(curNode.val)
                return
            
            # Call for left & right nodes
            dfs(curNode.left, leafSequence)
            dfs(curNode.right, leafSequence)
            
        # Function call
        seq1, seq2 = [], []
        dfs(root1, seq1)
        dfs(root2, seq2)

        # return
        return seq1 == seq2