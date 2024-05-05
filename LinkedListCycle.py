# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Base Case
        if head is None: return False

        # Set fast and slow pointer
        p1 = head
        p2 = p1

        # Iterate
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        
        # return
        return False