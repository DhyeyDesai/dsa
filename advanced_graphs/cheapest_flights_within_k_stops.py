# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# INTUITION:
# We want to find the cheapest flight path from src to dst with at most K stops.
# Think of this as exploring paths layer by layer, where each layer represents
# taking one more flight. We use a modified Bellman-Ford algorithm that relaxes
# edges exactly K+1 times (since K stops = K+1 flights).

# KEY INSIGHT: We copy the prices array each round to ensure we only use costs
# from the previous "layer" of stops. This prevents us from accidentally using
# a path that takes more than K stops in a single iteration.

# TIME COMPLEXITY: O(K * E) where E is the number of flights
# - We iterate K+1 times (outer loop)
# - Each iteration processes all E flights (inner loop)

# SPACE COMPLEXITY: O(N) where N is the number of cities
# - We maintain two arrays of size N (prices and tmpPrices)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize prices array: prices[i] = minimum cost to reach city i
        prices = [float("inf")] * n
        prices[src] = 0 # Cost to reach source is 0 (we start here)

        # Iterate K+1 times because K stops means we can take K+1 flights
        # Each iteration represents: "What's the best price if I take one more flight?"
        for i in range(k + 1):
            # Create a copy to store updates for this round
            # CRITICAL: This prevents us from using prices updated in the SAME round,
            # which would allow paths with more than K stops
            tmpPrices = prices.copy()

            # Try relaxing every flight edge
            for s, d, p in flights:  # s=source, d=dest, p=price
                # Skip if we haven't reached the source city yet
                # (can't take a flight from a city we haven't reached)
                if prices[s] == float("inf"):
                    continue
                
                # Relaxation step: if flying from s to d gives us a cheaper path
                # to city d, update the temporary prices
                # We check: current_cost_to_s + flight_price < current_best_to_d
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            # Update prices with the new minimum costs found in this round
            # This becomes the baseline for the next iteration
            prices = tmpPrices


        # If destination is still unreachable (infinity), return -1
        # Otherwise, return the minimum price to reach destination within K stops
        return -1 if prices[dst] == float("inf") else prices[dst]