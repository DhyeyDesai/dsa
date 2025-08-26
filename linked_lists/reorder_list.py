# 143. Reorder List
# https://leetcode.com/problems/reorder-list/description/

"""
Intuition:
To reorder L0→L1→L2→...→Ln-1→Ln into L0→Ln→L1→Ln-1→L2→Ln-2→..., we need to:
1. Split the list into two halves
2. Reverse the second half
3. Merge the two halves by alternating nodes

This is a classic three-step linked list problem that combines:
- Finding the middle (tortoise and hare)
- Reversing a linked list
- Merging two lists in alternating fashion

The key insight is that after reversing the second half, we can easily alternate
between the first and reversed second half to achieve the desired pattern.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Step 1: Find the middle of the list using slow/fast pointers
        slow = fast = head

        while fast and fast.next:
            slow = slow.next        # Move 1 step
            fast = fast.next.next   # Move 2 steps
        
        # At this point, slow is at the middle (or start of second half)
        
        # Step 2: Reverse the second half of the list
        second = slow.next    # Start of second half
        prev = slow.next = None  # Cut the list in half and initialize prev for reversal

        # Reverse the second half using standard reversal technique
        while second:
            tmp = second.next      # Store next node before we lose it
            second.next = prev     # Reverse the link
            prev = second          # Move prev forward
            second = tmp           # Move to next node
        
        # After reversal, prev points to the head of reversed second half
        
        # Step 3: Merge the first half and reversed second half alternately
        first, second = head, prev
        
        # Alternate nodes from first and second halves
        while second:  # Continue while second half has nodes
            # Store next nodes before we modify pointers
            tmp1, tmp2 = first.next, second.next
            
            # Connect: first → second → first.next
            first.next = second
            second.next = tmp1
            
            # Move to next pair of nodes
            first, second = tmp1, tmp2