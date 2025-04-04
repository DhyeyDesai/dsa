# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 1: Using DFS - recursive method

class Solution:
    def flatten(self, root):
        # perform DFS
        def dfs(root):
            if not root:
                return None
            # Save left and right tail at each node
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If a left node exists, it means a leftTail also exists.
            # Point the right pointer of the leftTail to the right node of the current node.
            if root.left:
                leftTail.right = root.right
                
                # Point the right pointer of the current node to the left node.
                # and point left pointer to null 
                root.right = root.left
                root.left = None
            
            # The last node in this recursion will be rightTail otherwise leftTail or the current node itself.
            last = rightTail or leftTail or root
            return last
        # Don't return anything since we are modifying the tree in-place.
        dfs(root)


# Solution 2: Iterative method

class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        while current:
            # If a left subtree exists, save the left node in a variable 'pre' which 
            # marks the start of the left-subtree
            if current.left:
                pre = current.left

                # If a right subtree of 'pre' exists, find the rightmost end of it using a while loop.
                while pre.right:
                    pre = pre.right

                # Once you have the rightmost node, point the right pointer to the 'current' node's right node.
                pre.right = current.right

                # Point the right pointer of current to its left node, and point the left pointer to null.
                current.right = current.left
                current.left = None
            
            # Move to the right pointer.
            current = current.right
    
        