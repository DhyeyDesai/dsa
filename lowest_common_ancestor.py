# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the root is None, return None (no ancestor exists).
        if root is None:
            return None
        
        # If the current node is either p or q, return it as a potential ancestor.
        if root == p or root == q:
            return root
        
        # Recursively search for p and q in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, it means p is found in one subtree
        # and q is found in the other, making the current node their lowest common ancestor.
        if left and right:
            return root
        
        # If only one of left or right is non-null, return the non-null value
        # as it contains one of the nodes (p or q) or their ancestor. 
        # Otherwise return None if neither exists.
        return left or right