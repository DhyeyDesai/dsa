# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

"""
Intuition:
The optimal approach is divide-and-conquer using pairwise merging. Instead of merging
all lists sequentially (which would be O(k*n*k) time), we merge lists in pairs 
repeatedly until only one remains. This reduces time complexity to O(n*k*log k).

The strategy:
1. Pair up adjacent lists and merge each pair
2. Replace the original list with these merged results  
3. Repeat until only one list remains

This is like a tournament bracket - we halve the number of lists each round.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edge case: empty input
        if len(lists) == 0:
            return None
        
        # Keep merging pairs until only one list remains
        while len(lists) > 1:
            mergedLists = []

            # Process lists in pairs (step by 2)
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair
                l2 = None      # Second list (might not exist for odd-length arrays)

                # Check if there's a second list to pair with
                if i + 1 < len(lists):
                    l2 = lists[i + 1]

                # Merge the pair (l1 with l2, or just l1 if l2 is None)
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Replace original lists with merged results for next iteration
            lists = mergedLists

        # After all iterations, only one merged list remains
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        """
        Helper function to merge two sorted linked lists.
        Uses dummy node technique for cleaner code.
        """
        # Create dummy node to simplify edge cases
        dummy = ListNode()
        curr = dummy

        # Merge nodes while both lists have elements
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1  # Connect to smaller node
                l1 = l1.next   # Advance l1 pointer
            else:
                curr.next = l2  # Connect to smaller node
                l2 = l2.next   # Advance l2 pointer
            curr = curr.next   # Move current pointer forward
        
        # Append remaining nodes (at most one list will have remaining nodes)
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        # Return merged list (skip dummy node)
        return dummy.next