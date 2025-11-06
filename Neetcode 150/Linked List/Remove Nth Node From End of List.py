from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # Intuition
        # Case for singe node:
        if head.next == None:
            return None
        
        # Reverse LinkedList
        head = self.reverseLinkedList(head)

        # Remove nth node:
        prev = None
        curr = head
        for i in range(n - 1):
            prev = curr
            curr = curr.next

        if prev is None:
            head = curr.next
        else:
            prev.next = curr.next

        # Reverse LinkedList
        return self.reverseLinkedList(head)
        
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # Two pointer method
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right != None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
# Intuition:
# Reverse LinkedList (O(n) time)
# Remove nth node (indexing from 1) (O(n) time)
# Reverse LinkedList (O(n) time)

# Build a linked list from a list
def listToLinkedList(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert linked list back to list for printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test
LinkedList = [1, 2]

head = listToLinkedList(LinkedList)

print("Before:", linked_list_to_list(head))  # [1, 2]

Solution().removeNthFromEnd(head, 1)
print("After:", linked_list_to_list(head))  # should be [1]