# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Intuition:
# 1. Move from left to right in each level until you reach the end (null).
# 2. While moving, connect the left child to the right child of the current node.
# 3. Connect the right child of the current node to left child of the next node.
# 4. Once you reach the end of the level, move to the next level

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base case
        if root is None:
            return None
        
        # Initialize a variable to track the leftmost node of each level.
        leftMost = root

        # Traverse each level, starting from the root.
        while leftMost.left:

            # Start at the leftmost node of the current level.
            current = leftMost

            while current:
                # Connect left child to the right child of the same node.
                current.left.next = current.right

                # If the current node has a next pointer, connect its right child
                # to the left child of the next node.
                if current.next:
                    current.right.next = current.next.left

                # Move to the next node in the current level.
                current = current.next

            # Move down one level, setting leftMost to its left child.
            leftMost = leftMost.left
        
        # Return the root of the tree after connecting all next pointers.
        return root

