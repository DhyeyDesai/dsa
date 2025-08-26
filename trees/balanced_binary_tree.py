# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Intuition:
# A tree is balanced if, at every node, the height difference between left and right subtrees 
# is at most 1, and both subtrees are also balanced. 
# We can compute height and balance status in a single DFS traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case: empty tree has height 0 and is balanced
            if root is None:
                return (0, True)
            
            # Recursively check left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            
            # A node is balanced if:
            # 1. Left and right subtrees are balanced
            # 2. Height difference <= 1
            balanced = abs(left[0] - right[0]) <= 1 and left[1] and right[1]
            
            # Return current height and balance status
            return (max(left[0], right[0]) + 1, balanced)
        
        # Return only the balance status of the whole tree
        return dfs(root)[1]

    
        
        