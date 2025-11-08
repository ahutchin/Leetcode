# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def DFS(root: TreeNode, maxVal: int) -> None:
            nonlocal goodNodes

            if not root:
                return
            
            if root.val >= maxVal:
                goodNodes += 1
                maxVal = root.val
            
            DFS(root.left, maxVal)
            DFS(root.right, maxVal)
        
        DFS(root, root.val)
        return goodNodes
            
# Intuition:
# dfs where we keep track of the current max node in the sequence, if the current node is greater than or equal to the max, we increment goodNodes by one
# Time Complexity: O(n) because we visit each node in the tree once
# Space Complexity: O(h) because the recursive calls create a recusrive stack of height h