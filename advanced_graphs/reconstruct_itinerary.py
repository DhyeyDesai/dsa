# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/description/

"""
SOLUTION 1: Backtracking DFS (Gets TLE)

INTUITION:
- Try to build the itinerary path from start to finish
- At each airport, try visiting destinations in lexicographical order
- If we reach a dead end (can't use all tickets), backtrack and try another path
- This is like trying different routes until we find one that uses all tickets

TIME COMPLEXITY: O(E^d) where E is number of tickets, d is maximum number of flights from an airport
- In worst case, we might explore many invalid paths before finding the correct one
- Each backtrack involves list operations (pop/insert) which are O(n)
- Exponential time due to trying multiple paths

SPACE COMPLEXITY: O(E)
- adj dictionary stores all tickets: O(E)
- res stores the path: O(E)
- Recursion stack depth: O(E)
"""
class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list with empty lists for each source airport
        adj = {src: [] for src, dst in tickets}
        
        # Sort tickets to ensure lexicographical order
        tickets.sort()

        # Populate adjacency list with destinations
        for src, dst in tickets:
            adj[src].append(dst)

        # Start the itinerary at JFK
        res = ["JFK"]

        def dfs(src):
            # Base case: if we've used all tickets, we found valid itinerary
            if len(res) == len(tickets) + 1: 
                return True

            # If current airport has no outgoing flights, it's a dead end
            if src not in adj:
                return False
            
            # Try each destination from current airport
            temp = list(adj[src])  # Create copy to iterate safely
            for i, v in enumerate(temp):
                # Use this ticket (remove from available tickets)
                adj[src].pop(i)
                res.append(v)
                
                # Recursively try to complete itinerary from this destination
                if dfs(v): 
                    return True
                
                # Backtrack: this path didn't work, restore the ticket
                adj[src].insert(i, v)  # O(n) operation - causes slowness!
                res.pop()

            # No valid path found from this airport
            return False

        dfs("JFK")
        return res


"""
SOLUTION 2: Hierholzer's Algorithm (Optimal)

INTUITION:
- This problem is finding an Eulerian path (visit every edge exactly once)
- Instead of building path forward, we build it BACKWARDS
- We go deep into the graph, exhausting all edges from each node
- Only after visiting all destinations from an airport do we add it to result
- Think of it like: "I can only write down where I am after I've explored all paths from here"
- Dead ends (airports with no outgoing flights) naturally get added first

EXAMPLE VISUALIZATION:
If path is: JFK → A → B → C → A → D
We explore: JFK → A → B → C → A → D (until stuck)
We record: D, then A, then C, then B, then A, then JFK (backwards!)
Then reverse to get correct order.

TIME COMPLEXITY: O(E log E) where E is number of tickets
- Sorting tickets: O(E log E)
- Building adjacency list: O(E)
- DFS visits each edge exactly once: O(E)
- Reversing result: O(E)
- Overall: O(E log E)

SPACE COMPLEXITY: O(E)
- adj dictionary stores all tickets: O(E)
- res stores the path: O(E)
- Recursion stack depth in worst case: O(E)
"""
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list using defaultdict for cleaner code
        adj = defaultdict(list)
        
        # Sort tickets lexicographically, then reverse
        # This way when we pop() from the list, we get smallest destination first
        # Example: [JFK→ATL, JFK→SFO] → sorted → reversed to [SFO, ATL]
        # pop() gives ATL (lexicographically smaller)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        
        def dfs(src):
            # Keep exploring while current airport has outgoing flights
            while adj[src]:
                # Take the next destination (smallest lexicographically due to our reversed sorting)
                dst = adj[src].pop()
                
                # Recursively visit that destination and exhaust all its paths
                dfs(dst)
            
            # Only add current airport to result AFTER exhausting all its outgoing edges
            # This builds the path in reverse order
            res.append(src)

        # Start DFS from JFK
        dfs('JFK')
        
        # Reverse to get the correct order (we built it backwards)
        return res[::-1]