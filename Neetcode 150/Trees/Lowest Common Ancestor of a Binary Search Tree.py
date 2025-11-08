# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if min(p.val, q.val) <= root.val <= max(p.val,q.val):
            return root
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)

# Intuition:
# Find p and q -> work up the tree until the routes intersect
# The intersection occurs when p =< currNode.val =< q
# Time Complexity: O(h)
# Space Complexity: O(h)
