# 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Intuition - Each level is an array. If the parent's index is n, it's children have indices 2n and 2n+1.
# 1. perform BFS
# 2. keep track of indices of the first and last non-null elements.
# 3. width of any level = last element index - first element index + 1
# 4. compare with maxWidth global variable
 
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxWidth = 1

        # Create a queue for BFS, where each element is a tuple of two items - the node and 
        # its index in its level
        q = deque([(root, 0)])

        while len(q):
            
            # append new nodes in the queue for the next level of BFS
            for i in range(len(q)):
                node, index = q.popleft()

                # the first non-null element of each level is the left-index
                #  and the width is measured starting from that index
                if i == 0:
                    leftIndex = index                
                if node.left:
                    q.append((node.left, 2*index))
                if node.right:
                    q.append((node.right, 2*index+1))

            # save the index of rightmost non-null element to measure the width of that level
            rightIndex = index
            # find out the current width and see if its the max width yet.
            currentWidth  = rightIndex - leftIndex + 1
            maxWidth = max(currentWidth, maxWidth)
        return maxWidth