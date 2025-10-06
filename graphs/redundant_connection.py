# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/


# Intuition:
# A valid tree with N nodes must have exactly N-1 edges. Here, we are given N edges,
# which guarantees that one edge is creating a cycle.
# We use Union-Find (Disjoint Set Union) to simulate connecting nodes one-by-one.
# If an edge tries to connect two nodes that already share the same root (parent),
# then that edge introduces a cycle → this is our redundant connection.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # Initially, every node is its own parent (self-rooted)
        parent = [i for i in range(n + 1)]
        
        # Rank represents the size/weight of each tree to help union by rank
        rank = [1] * (n + 1)

        # Find with path compression: keeps tree flat by linking nodes to root directly
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])  # path compression
            return parent[node]

        # Union two sets; return False if they are already connected (cycle detected)
        def union(node1, node2):
            # Find the root parents of both nodes
            root1, root2 = find(node1), find(node2)

            # If both nodes already share the same root, then they are already connected.
            # Trying to connect them again would form a cycle, so we return False.
            if root1 == root2:
                return False
            
            # Otherwise, we merge smaller tree into larger (union by rank)
            # ============================
            # UNION BY RANK EXPLAINED:
            # ============================
            # - 'rank' roughly represents the *height* or *size* of the tree.
            # - To keep trees shallow (which makes future find() operations faster),
            #   we always attach the *smaller tree* under the *larger tree*.
            # - This avoids creating long chains of parents, ensuring near O(1) operations.
            #
            # Example:
            #   If root_a's tree has rank 3 and root_b's tree has rank 1,
            #   attaching root_b under root_a keeps the overall depth unchanged.
            # ============================
            if rank[root1] > rank[root2]:
                # root1 has a larger tree → attach root2 under root1
                parent[root2] = root1
                rank[root1] += rank[root2] # Increase the size of root1's tree
            elif rank[root1] < rank[root2]:
                # root2 has a larger tree → attach root1 under root2
                parent[root1] = root2
                rank[root2] += rank[root1] # Increase the size of root2's tree
            else:
                # Both trees have equal rank → merge arbitrarily (attach root2 under root1)        
                parent[root2] = root1
                rank[root1] += 1 # Increase rank *only by 1* since depth grows by one level

            return True

        # Try to union each edge; the one that fails is the redundant one
        for u, v in edges:
            if not union(u, v):
                return [u, v]
