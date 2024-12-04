# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case:
        if root is None or root is p or root is q:
            return root
                
        # recursive call on children
        leftTree = self.lowestCommonAncestor(root.left, p, q)
        rightTree = self.lowestCommonAncestor(root.right, p, q)

        # return
        if rightTree is None: 
            return leftTree
        if leftTree is None:
            return rightTree
        
        return root
    
# Time Complexity: O(n) because we visit each node at most once
# Space Complexity: O(1) doesnt use any additional space