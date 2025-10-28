# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


# Intuition:
# The maximum depth of a binary tree is the longest path from root to a leaf.
# Two common ways to compute this:
# 1. Recursive DFS: depth = 1 + max(depth(left), depth(right))
# 2. BFS: level-order traversal, counting how many levels we traverse.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive DFS Method    
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: empty tree has depth 0
        
        # Depth is 1 (current node) + max depth of left/right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

# BFS (Level Order) Method
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0  # Tracks number of levels (tree depth)
        while q:
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1  # Finished one level
        return level