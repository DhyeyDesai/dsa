# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (0, True)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            balanced = abs(left[0]-right[0])<=1 and left[1] and right[1]
            
            return (max(left[0], right[0]) + 1, balanced)
        
        return dfs(root)[1]
    
        
        