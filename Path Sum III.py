from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Car definition
        cache = defaultdict(int)
        cache[0] = 1
        self.result = 0

        # dfs algorithm
        def dfs(node: Optional[TreeNode], curSum: int, target: int, cache: dict):
            # Basecase
            if node is None:
                return
            
            # Update curSum
            curSum += node.val
            
            # Check if curSum - target exists in cache
            self.result += cache.get(curSum - target, 0)

            # Update cache with new curSum
            cache[curSum] += 1

            # Call dfs on children
            dfs(node.left, curSum, target, cache)
            dfs(node.right, curSum, target, cache)

            # remove curSum from cache when done with branch
            cache[curSum] -= 1
        
        dfs(root, 0, targetSum, cache)

        return self.result
    
# test
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

# Tree values in level-order as given in the problem
tree_values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = build_tree(tree_values)

# Test
test = Solution()
result = test.pathSum(root, 22)
print(result)  