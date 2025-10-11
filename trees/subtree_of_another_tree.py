# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# TODO: figure out a O(m+n) time solution using serialization

# Intuition: For each node in the main tree, check if the tree rooted at that node
# is identical to subRoot. We traverse the main tree and at each node, perform
# a full tree comparison to see if it matches subRoot structurally and by values.

# Time Complexity: O(m * n) where m is the number of nodes in root, n in subRoot
#   - We visit each node in root once: O(m)
#   - At each node, we might compare trees: O(n)
#   - Worst case: O(m * n)
# Space Complexity: O(h1 + h2) where h1 is height of root, h2 is height of subRoot
#   - Recursion stack for isSubtree: O(h1)
#   - Recursion stack for compareTrees: O(h2)
#   - These can overlap, so effectively O(max(h1, h2)) in practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge cases: null subRoot is always a subtree, null root with non-null subRoot is not
        if not subRoot:
            return True
        if not root:
            return False
        # Check if trees rooted at current node are identical
        if self.compareTrees(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compareTrees(self, node1, node2):
        # Both null: trees are identical
        if not node1 and not node2:
            return True
        # Both exist and values are similar: Check their left and right subtrees
        if node1 and node2 and node1.val == node2.val:
            left = self.compareTrees(node1.left, node2.left)
            right = self.compareTrees(node1.right, node2.right)
            return left and right
        return False