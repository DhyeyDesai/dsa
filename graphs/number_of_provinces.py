# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    # INTUITION:
    # Use Union-Find to merge connected cities into provinces. Start with n provinces
    # (each city is its own province). For each direct connection in the adjacency 
    # matrix, union the two cities. Each successful merge reduces province count by 1.
    # Process only upper triangle to avoid duplicates, and stop early if all merge into one.

    # TIME COMPLEXITY: O(n² × α(n)) ≈ O(n²)
    # - Worst case: check all n(n-1)/2 pairs in upper triangle
    # - Each union/find: O(α(n)) ≈ O(1) with path compression
    # - Best case with early termination: O(E × α(n)) where E << n²

    # SPACE COMPLEXITY: O(n)
    # - par array: O(n)
    # - rank array: O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        # Track size of each tree for union by rank
        rank = [1] * n

        # Each city starts as its own parent (separate province)
        par = [i for i in range(n)]

        def find(n1):
            # Find root parent with path compression
            res = n1
            
            # Traverse up to root, flattening tree along the way
            while res != par[res]:
                par[res] = par[par[res]] # Path compression
                res = par[res]
            
            return res

        def union(n1, n2):
            # Union two provinces. Returns 1 if merged, 0 if already connected.
            p1 = find(n1)
            p2 = find(n2)

            # Already in same province, no merge needed
            if p1 == p2:
                return 0
            
            # Union by rank: attach smaller tree under larger tree
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return 1

        # Start with n separate provinces 
        res = n
        
        # Process only upper triangle (avoid duplicates and self-loops)
        for i in range(n):
            for j in range(i+1, n): # j > i ensures we check each pair once
                if isConnected[i][j] == 1:
                    # Try to merge these two cities' provinces
                    res -= union(i, j)

                    # Early termination: if all cities merged into one province, done!
                    if res == 1:
                        return 1
        return res