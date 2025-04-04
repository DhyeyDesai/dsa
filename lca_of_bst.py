# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Intuition:
# In a Binary Search Tree (BST), all values in the left subtree are smaller, and all values in the right subtree are larger.
# If both p and q are greater than the current node, their Lowest Common Ancestor (LCA) must be in the right subtree.
# If both p and q are smaller than the current node, their LCA must be in the left subtree.
# If one value is smaller and the other is greater (or the current node is equal to p or q), this means the current node is the LCA, as it's the first point where p and q diverge.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       while root:
            # If both p and q are greater than the current node, move to the right subtree.
            if min(p.val, q.val) > root.val:
               root = root.right

            # If both p and q are smaller than the current node, move to the left subtree.
            elif max(p.val, q.val) < root.val:
                root = root.left
            
            # If p and q are on different sides (or one of them matches the current node),
            # the current node is their lowest common ancestor.
            else:
                return root
            
# Note: We could have also used the same method as in the Lowest Common Ancestor of Binary Tree problem (solution at ./lowest_common_ancestor.py), but here we took advantage of the BST property(all values in left subtree are smaller and all values in the right subtree are larger than the current node) to make it simpler. 