# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Intuition:
# 1. Calculate total length to determine how many complete k-groups exist
# 2. For each k-group, reverse nodes using standard reversal (prev/curr/next pointers)
# 3. Track the tail of the previous group to connect it to the new head of current reversed group
# 4. The original head of each group becomes its tail after reversal, connecting to next group
#
# Time Complexity: O(n) - two passes through the list (count length + reverse)
# Space Complexity: O(1) - only using pointers, no extra data structures

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Dummy node simplifies edge cases (when head changes)
        dummy = ListNode(0, head)        
        
        # Count total nodes to determine number of complete k-groups
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        n = length // k  # Number of complete groups to reverse

        # Track the tail of the previous group for connection
        prevGroupTail = dummy
        curr = head

        # Process each complete k-group
        for _ in range(n):
            
            # Standard reversal setup
            prev = None
            newTail = curr  # Current head becomes tail after reversal

            # Reverse k nodes in current group
            for _ in range(k):
                nxt = curr.next
                curr.next = prev  # Reverse the link
                prev = curr
                curr = nxt
            
            # Connect previous group's tail to new head (prev) of reversed group
            prevGroupTail.next = prev
            # Connect new tail to the start of next group (curr)
            newTail.next = curr
            # Move prevGroupTail forward for next iteration
            prevGroupTail = newTail

        # Return new head (skip dummy node)
        return dummy.next