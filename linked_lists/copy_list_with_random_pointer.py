# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Intuition:
# The challenge is that we need to copy nodes that have both next and random pointers,
# where random can point to any node in the list (or None). We can't set the random
# pointers during the first pass because the target nodes might not exist yet. 

# Solution: Two-pass approach with a hashmap. First pass creates all new nodes and
# maps old→new. Second pass sets up all the pointers using the mapping. The key
# insight is initializing the map with {None: None} to handle edge cases cleanly.


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # HashMap to store mapping from original nodes to their copies
        # Initialize with {None: None} to handle edge cases (when next/random is None)
        oldToCopy = {None: None}

        # First pass: Create all new nodes and build the mapping
        cur = head
        while cur:
            # Create a new node with the same value
            copy = Node(cur.val)
            # Map the original node to its copy
            oldToCopy[cur] = copy
            cur = cur.next
        
        # Second pass: Set up next and random pointers for all copied nodes
        cur = head
        while cur:
            # Get the copied version of the current node
            copy = oldToCopy[cur]
            
            # Set next pointer: copy.next should point to the copy of cur.next
            copy.next = oldToCopy[cur.next]
            
            # Set random pointer: copy.random should point to the copy of cur.random
            copy.random = oldToCopy[cur.random]
            
            cur = cur.next

        # Return the head of the copied list
        return oldToCopy[head]