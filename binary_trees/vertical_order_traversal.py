# link - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        # create a dict to keep track of nodes based on their x-coordinate
        locationMap = defaultdict(list)
        
        # create a queue where each element is a tuple
        queue = deque([(0,0, root)]) # (x-coordinate, y-coordinate, node)

        # perform BFS
        while len(queue):
            for i in range(len(queue)):
                x,y, current = queue.popleft()
                
                # append the y-coordinate(level) and current node value to the corresponding x-coordinate in the location map dict
                locationMap[x].append((y, current.val)) 

                # increment y value(level) and decrement x value for left child node or increment x value for right child node
                if current.left:
                    queue.append((x-1, y+1, current.left))
                if current.right:
                    queue.append((x+1, y+1, current.right))
        result = []

        # sort the locationMap dict based on keys, meaning we move from left to right on x-axis
        for column in sorted(locationMap.keys()):
             # Sort the values for each x-coordinate in the dict.
             # Since each tuple is a pair of y-coordinate(level) and node value, 
             # it sorts each level by values in case of a similar X and a Y coordinate.
            nodes = sorted(locationMap[column])

            # add all values to the result list, column by column.
            result.append([val for i, val in nodes])
        return result