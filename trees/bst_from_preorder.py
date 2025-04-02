# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Return null if the list is empty.
        if not preorder:
            return None
        
        # Initialize the root node with the first element of the preorder list.
        root = TreeNode(val = preorder[0])

        # Create a stack with the root node as the first element.
        stack = [root]

        # Iterate through the remaining elements.
        for item in preorder[1:]:
            itemNode = TreeNode(val = item)

            # If the value is smaller than the top node's value, 
            # it must be placed in the left subtree of the top node.
            if item < stack[-1].val:
                stack[-1].left = itemNode
                stack.append(itemNode)

            # Otherwise, find the correct parent node for this value by popping from the stack.
            # The first popped node with a value smaller than the current item will be its parent,
            # and the new node should be placed in its right subtree.
            else:
                while stack and item > stack[-1].val:
                    node = stack.pop()
                node.right = itemNode
                stack.append(itemNode)
        return root
                

