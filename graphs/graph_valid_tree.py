# NOTE: This is a premium problem. We will use a similar problem from neetcode.io

# 178. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/

# NeetCode - Graph Valid Tree
# https://neetcode.io/problems/valid-tree/question?list=neetcode150

"""
INTUITION:
A valid tree must satisfy two conditions:
1. The graph must be fully connected (all nodes reachable from any starting node)
2. There must be no cycles (exactly n-1 edges for n nodes, and no back edges)

We use DFS to detect cycles by tracking the previous node we came from. If we visit
a node that's already been visited AND it's not the node we just came from, we found
a cycle. After DFS, we verify all nodes were visited (connected graph).

TIME COMPLEXITY: O(n + e) where n = number of nodes, e = number of edges
- We visit each node once: O(n)
- We traverse each edge twice (undirected graph): O(e)

SPACE COMPLEXITY: O(n + e)
- Adjacency list storage: O(n + e)
- Visited set: O(n)
- Recursion stack (worst case): O(n)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case: empty graph is considered a valid tree
        if not n:
            return True
        
        # Build adjacency list representation of the graph
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)  # Undirected graph, so add both directions

        # Track visited nodes to detect cycles and count connectivity
        visit = set()
        
        def dfs(i, prev):
            # If we've already visited this node, we found a cycle
            if i in visit:
                return False
            
            # Mark current node as visited
            visit.add(i)
            
            # Explore all neighbors
            for j in adj[i]:
                # Skip the node we just came from (parent in DFS tree)
                # This prevents false cycle detection in undirected graphs
                if j == prev:
                    continue
                
                # Recursively visit neighbor; if cycle found, propagate False
                if not dfs(j, i):
                    return False
            
            # No cycle found in this path
            return True

        # Check two conditions:
        # 1. dfs(0, -1): No cycles exist (starting from node 0, no previous node)
        # 2. len(visit) == n: All nodes are connected (we visited every node)
        return dfs(0, -1) and len(visit) == n