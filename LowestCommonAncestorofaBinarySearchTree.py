# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Intuition is to traverse from p and q upward until we find a match, likely need to store visited node info somehow
        # We must utilize the fact that the tree is sorted

        currentNode =  root

        while currentNode:
            if p.val < currentNode.val and q.val < currentNode.val: 
                currentNode = currentNode.left
            elif p.val > currentNode.val and q.val > currentNode.val: 
                currentNode = currentNode.right
            else: 
                return currentNode