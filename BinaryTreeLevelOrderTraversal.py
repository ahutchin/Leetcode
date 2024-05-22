from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Intuition: This is basically BFS 
# it can be done recursively or with a Queue
class Solution:
    # Time Complexity: O(n) because we visit each node once
    # Space Complexity: O(n) because the queue will have a maximum of n/2 nodes in it at one time
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Define queue and result list
        result = []
        queue = []

        queue.append(root)

        # Iterate while there are items in the queue
        while queue:
            level = [] # The list of nodes to be added to the result list

            # Keep track of initial queue length to control for the level
            lengthQ = len(queue)
            for i in range(lengthQ):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            # Add level list to result
            if level: # Only add if there are items
                result.append(level)

        # return
        return result