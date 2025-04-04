# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If the list is empty, return None (no node to create).
        if not nums:
            return None
        
        # Find the middle index of the array.
        mid = len(nums)//2

        # Create a root node with the middle element as its value.
        root = TreeNode(nums[mid])

        # Recursively build the left subtree with the left half of the array.
        # The left child of the current root node will be the root of the left subtree.
        root.left = self.sortedArrayToBST(nums[:mid])

        # Recursively build the right subtree with the right half of the array.
        # The right child of the current root node will be the root of the right subtree.
        root.right = self.sortedArrayToBST(nums[mid+1:])

        # Return the root node after building the entire tree.
        return root