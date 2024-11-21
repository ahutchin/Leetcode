from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case
        if root is None:
            return None
        
        # Check node val
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)

# Test
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kid_nodes = nodes[::-1]
    root = kid_nodes.pop()
    
    for node in nodes:
        if node:
            if kid_nodes: node.left = kid_nodes.pop()
            if kid_nodes: node.right = kid_nodes.pop()
    return root

root = build_tree([4,2,7,1,3])

test = Solution()
result = test.searchBST(root, 2)
print(result)

# O(h) (height of the tree) time complexity, worst case O(n)
# O(1) space complexity (doesnt use any more space)