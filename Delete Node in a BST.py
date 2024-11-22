from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Define helpers
        def findSuccessor(node: Optional[TreeNode]) -> TreeNode:
            while node.left is not None:
                node = node.left
            
            return node
        
        def deleteSuccessor(node: Optional[TreeNode]) -> int:
            if node is None:
                return None
            
            if node.left is None:
                temp = node.right
                node = None
                return temp
            
            node.left = deleteSuccessor(node.left)
            return node

        # step 1: Locate node
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # step 2: Delete Node
        if key == root.val:
            if (root.left is None) and (root.right is None):
                root = None
                return None
            elif (root.left is None):
                temp = root.right
                root = None
                return temp
            elif (root.right is None):
                temp = root.left
                root = None
                return temp
            
            successor = findSuccessor(root.right)
            root.val = successor.val
            root.right = deleteSuccessor(root.right)

        # return
        return root

# O(h) time where h is height of the tree, so worst case O(n) and best case O(logn)