# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)

            neighbors = node.neighbors
            for bor in neighbors:
                copy.neighbors.append(dfs(bor))
            
            return copy
        return dfs(node) if node else None

    
from collections import deque
class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        
        queue = deque()
        queue.append(node)

        while queue:
            current = queue.popleft()

            for nei in current.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)
                oldToNew[current].neighbors.append(oldToNew[nei])
        
        return oldToNew[node]
        