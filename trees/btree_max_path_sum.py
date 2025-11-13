# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Intuition:
# 1. A path can start and end at any node, going through their lowest common ancestor
# 2. At each node, we have a choice: include it in a path with left subtree, right subtree, or both
# 3. For the global answer, we consider the path that splits at current node (left + node + right)
# 4. For recursion, we return the maximum single-branch path (node + max(left, right)) to parent
# 5. We ignore negative paths by taking max with 0 (better to not include them)

# Time Complexity: O(n) where n is the number of nodes
#   - We visit each node exactly once in the DFS traversal
# Space Complexity: O(h) where h is the height of the tree
#   - Recursion call stack depth equals tree height
#   - Worst case (skewed tree): O(n)
#   - Best case (balanced tree): O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val
        # Or use list without nonlocal to allow modification in nested function (mutable container)
        # res = [root.val]
        # and return and modify res[0]
        
        def dfs(node):
            nonlocal res 

            # Base case: null node contributes 0 to any path
            if not node:
                return 0
            
            # Recursively get max path sum from left and right subtrees
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # Ignore negative paths - better to not include them at all
            # If a subtree gives negative sum, treat it as 0 (don't take that path)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Update global maximum with path that splits at current node
            # This considers: left subtree + current node + right subtree
            res = max(res, leftMax + rightMax + node.val)
            
            # Return max single-branch path for parent to use
            # Parent can only extend one branch (either left or right, not both)
            return node.val + max(leftMax, rightMax)
         
        dfs(root)
        return res