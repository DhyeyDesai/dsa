# Children Sum in a Binary Tree
# https://bit.ly/3dEr73g

# Node Class:
# class Node:
#     def init(self,val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    # Function to check whether all nodes of a tree have the value 
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):

        # Base case: If the current node is None return 1
        if root is None:
            return 1
        
        # If the node has at least one child, check the sum property.
        if root.left or root.right:
            # Assign 0 if a child node is None, otherwise use its data value.
            leftVal = root.left.data if root.left else 0
            rightVal = root.right.data if root.right else 0

            # Compute sum of left and right children
            childSum = leftVal+rightVal

            # The current node satisfies the condition if:
            # 1. Its value equals the sum of its children.
            # 2. Both left and right subtrees also satisfy the condition.
            if childSum == root.data and self.isSumProperty(root.left) == 1 and self.isSumProperty(root.right) == 1:
                return 1
            else:
                return 0
        
        # If the node is a leaf node, return 1 (since it satisfies the property trivially).
        return 1

        

