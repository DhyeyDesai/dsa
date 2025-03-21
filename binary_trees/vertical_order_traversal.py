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
        locationMap = defaultdict(list)
        queue = deque([(0,0, root)])
        while len(queue):
            for i in range(len(queue)):
                x,y, current = queue.popleft()
                locationMap[x].append((y, current.val))
                if current.left:
                    queue.append((x-1, y+1, current.left))
                if current.right:
                    queue.append((x+1, y+1, current.right))
        result = []
        for column in sorted(locationMap.keys()):
            nodes = sorted(locationMap[column])
            result.append([val for i, val in nodes])
        return result