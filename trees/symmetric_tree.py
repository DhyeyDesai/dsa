# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Intuition: 
# Two mirroring nodes should have the same value.
# Check if the left subtree and right subtree of the root node are mirror images of each other.
# To do this, we create a function to check whether they are mirrors of each other or not.
# We move in the opposite directions for both nodes and see if they are equal on both sides of the mirror.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Create isMirror function to check if mirroring nodes are same or not
        def isMirror(node1, node2):
            # both are none - return true
            if not node1 and not node2:
                return True
            
            # one of them is none and the other is not - return false
            if not node1 or not node2:
                return False
            

            # see if these conditions are fulfilled:
            # 1. both nodes have same values
            # 2. check if left child of first node and 
            #    right child of second node are symmetric.
            # 3. check if right child of first node and 
            #    left child of second node are symmetric.

            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        # pass left and right nodes to the isMirror function
        return isMirror(root.left, root.right)