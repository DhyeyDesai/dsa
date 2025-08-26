# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Intuition:
# The diameter of a binary tree is the longest path between any two nodes.
# At each node, the longest path through it is (height of left subtree + height of right subtree).
# We use DFS to compute subtree heights and update the maximum diameter as we go.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # Stores the maximum diameter found so far

        def dfs(node):
            nonlocal res
            if not node:
                return 0  # Base case: empty subtree has height 0

            # Recursively compute left and right subtree heights
            left = dfs(node.left)
            right = dfs(node.right)

            # Update diameter: longest path through current node
            res = max(res, left + right)

            # Return height of current subtree
            return max(left, right) + 1

        dfs(root)
        return res
