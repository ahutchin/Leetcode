# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Global vars
        res = [0]

        # Define dfs algorithm
        def dfs(currNode: TreeNode, currMax: int) -> None:
            # Base case
            if currNode is None: 
                return
            
            if currNode.val >= currMax:
                currMax = currNode.val
                res[0] += 1
            
            dfs(currNode.left, currMax)
            dfs(currNode.right, currMax)     
            return

        # Call dfs
        dfs(root, root.val)

        return res[0]