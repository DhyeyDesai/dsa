# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

# Intuition:
# This problem asks for the minimum time required for a signal sent from node K to reach ALL N nodes.
# This is equivalent to finding the single-source shortest path to all other nodes in the network,
# and the answer will be the time taken to reach the farthest node.
# We use Dijkstra's algorithm, implemented with a min-heap (priority queue),
# to efficiently explore the network and find the shortest travel time from the source node K
# to every other node.

# Time Complexity: O(E log V) or O(E log N), where E is the number of travel times (edges) and N is the number of nodes (vertices).
# Space Complexity: O(N + E) for storing the adjacency list (edges) and the set of visited nodes.

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list (graph) to store the edges.
        # Key: source node (u), Value: list of (target node (v), travel time (w)).
        edges = defaultdict(list)

        # Build the graph from the input 'times' list.
        for u, v, w in times:
            edges[u].append((v, w))
        
        # Initialize the min-heap (priority queue). It stores tuples of (time, node).
        # We start at node k with a time of 0.
        minHeap = [(0, k)]
        # 'visit' set tracks nodes for which we have finalized the shortest time.
        visit = set()
        # 't' will store the total time taken to reach the last visited node.
        t = 0
        
        # Dijkstra's main loop: continues as long as there are nodes to process in the heap.
        while minHeap:
            # Pop the node with the current shortest time from the source k.
            w1, n1 = heapq.heappop(minHeap)
            
            # If the node has already been visited (meaning we've found the shortest path to it), skip it.
            if n1 in visit:
                continue
            
            # Mark the current node as visited and record the time to reach it.
            # This 'w1' is the shortest time from k to n1.
            visit.add(n1)
            t = w1

            # Explore all neighbors (n2) of the current node (n1).
            for n2, w2 in edges[n1]:
                # Only consider neighbors that haven't had their shortest time finalized yet.
                if n2 not in visit:
                    # The time to reach the neighbor n2 through the current path (k -> ... -> n1 -> n2)
                    # is the time to reach n1 (w1) plus the time from n1 to n2 (w2).
                    # Push this new path (time, node) onto the heap.
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    
        # After the loop, check if all N nodes have been visited.
        # If 'len(visit) == n', it means the signal reached all nodes, and 't' is the time to reach the farthest one.
        # Otherwise, if 'len(visit) < n', some nodes are unreachable, and we return -1.
        return t if len(visit) == n else -1