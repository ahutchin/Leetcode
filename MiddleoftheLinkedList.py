from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize 2 pointers
        slow = head
        fast = head

        # Iterate
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Return
        return slow