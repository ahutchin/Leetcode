from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None: # Brute Force
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     currNode = head
    #     vals = []

    #     while currNode != None:
    #         vals.append(currNode.val)
    #         currNode = currNode.next
        
    #     currNode = head
    #     for i in range(len(vals)):
    #         if i % 2 == 1:
    #             currNode.val = vals[((i + 1) // 2) * -1 ]
    #         else:
    #             currNode.val = vals[i // 2]
    #         currNode = currNode.next
        
    def reorderList(self, head: Optional[ListNode]) -> None: # Optimal
        # Acquire midpoint of LinkedList
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse 2nd LinkedList
        second = slow.next
        slow.next = prev = None
        while second != None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Alternate merge the 2 Lists
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        

# Intuition
# This needs to be O(n) time (worst case) because the node count's range is [1, 10^4]

# Brute force:
# Iterate through list to get all node values
        
# Build a linked list from a list
def build_linked_list(values):
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

# Test it
head = build_linked_list([1, 2, 3, 4])
print("Before:", linked_list_to_list(head))  # [1, 2, 3, 4]

Solution().reorderList(head)
print("After:", linked_list_to_list(head))  # should be [1, 4, 2, 3]

# Brute force:
# Time Complexity: O(n)
# Space Complexity: O(n)
