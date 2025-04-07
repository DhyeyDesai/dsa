# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # Perform DFS
        def helper(root, memo):

            # Base case: return False if node is None
            if not root:
                return False
            
            # If k - root.val exists in the memo set, it means we have the other node required to achieve the target sum. So, return True.
            if (k - root.val) in memo:
                return True
            
            # Add the curent node value to the memo set.
            memo.add(root.val)

            # Recursively check if a pair to achieve target sum is found in either left or right subtree.
            return helper(root.left, memo) or helper(root.right, memo)
        
        # Initialize the set and pass it to the helper(DFS) function
        memo = set()
        return helper(root, memo)