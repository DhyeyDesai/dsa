# NOTE: This is a premium problem. We will use a similar problem from neetcode.io

# 323. Number of Connected Components In An Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# NeetCode - https://neetcode.io/problems/count-connected-components/question?list=neetcode150

# INTUITION:
# Use Union-Find to track connected components. Start with n separate components
# (each node is its own component). For each edge, try to union the two nodes.
# If they're already in the same component, nothing changes. If they're in 
# different components, merge them and decrement the component count.

# Think of it like: "How many separate friend groups exist if we connect 
# people based on the given relationships?"

# TIME COMPLEXITY: O(n + E * α(n)) ≈ O(n + E)
# - n to initialize par and rank arrays
# - E edges, each union/find operation is nearly O(1) due to optimizations
# - α(n) is inverse Ackermann function (practically constant, < 5 for real inputs)

# SPACE COMPLEXITY: O(n)
# - par array: O(n)
# - rank array: O(n)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize: each node is its own parent (self-loop)
        par = [i for i in range(n)]
        # Track the size/rank of each tree for union by rank optimization
        rank = [1] * n

        def find(n1):
            # Find the root parent of node n1 with path compression
            res = n1
            
            # Traverse up to find the root (where node == its own parent)
            while res != par[res]:
                # Path compression: make current node point to grandparent
                par[res] = par[par[res]]
                res = par[res]
            
            return res

        def union(n1, n2):
            # Union two nodes' components. Returns 1 if merged, 0 if already connected.
            # Uses union by rank to keep trees balanced.
            
            # Find root parents of both nodes
            p1, p2 = find(n1), find(n2)
            
            # Already in the same component, no merge needed
            if p1 == p2:
                return 0

            # Union by rank: attach smaller tree under larger tree
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]  # Update size
                par[p1] = p2          # Make p2 the parent
            else:
                rank[p1] += rank[p2]  # Update size
                par[p2] = p1          # Make p1 the parent
            
            # Successfully merged two components
            return 1

        # Start with n separate components
        res = n
        
        # Process each edge: try to union the two nodes
        for n1, n2 in edges:
            # If union successful (merged two components), decrement count
            res -= union(n1, n2)
        
        return res