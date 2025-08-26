# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Intuition:
# A "good" node is one that is greater than or equal to all values on the path from root to it.
# While traversing with DFS, keep track of the maximum value seen so far.
# If the current node's value >= max so far, it's a good node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            
            # Current node is "good" if its value is >= max seen so far
            res = 1 if root.val >= maxVal else 0
            
            # Update max for the path going down
            maxVal = max(root.val, maxVal)
            
            # Continue DFS on left and right children
            leftGood = dfs(root.left, maxVal)
            rightGood = dfs(root.right, maxVal)
            
            # Total good nodes in this subtree
            return leftGood + rightGood + res
        
        # Start DFS with root value as the initial max
        return dfs(root, root.val)