# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Intuition:
# Inverting a binary tree means swapping left and right children at every node.
# A simple recursive DFS works: at each node, swap its children, then recurse on them.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None  # Base case: empty subtree
        
        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

