# Top View of Binary Tree
# https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, data=0, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
class Solution:
    def topView(self, root):
        # create a dict to keep track of the top-most node of each column on x-axis
        locationMap = defaultdict(int)
        
        # create a queue where each element is a tuple
        queue = deque([(0,0, root)]) # (x-coordinate, y-coordinate, node)

        # perform BFS
        while len(queue):
            for i in range(len(queue)):
                x,y, current = queue.popleft()
                
                # update the top-most node of the current column with current node value in the location map dict
                # if an entry at the current x-coordinate is not present, add it to the locationMap
                # otherwise, skip the current node since we already need to keep track of the top-most node in each column
                if x not in locationMap:
                    locationMap[x] = current.data

                # increment y value(level) and decrement x value for left child node or increment x value for right child node
                if current.left:
                    queue.append((x-1, y+1, current.left))
                if current.right:
                    queue.append((x+1, y+1, current.right))
        result = []

        # sort the locationMap dict based on keys, meaning we move from left to right on x-axis
        for column in sorted(locationMap.keys()):
            # Fetch the bottom-most node in the column and append it to the result array
            node = locationMap[column]
            result.append(node)
        return result