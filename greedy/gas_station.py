# 134. Gas Station
# https://leetcode.com/problems/gas-station/description/

# Intuition:
# This problem uses a greedy approach with two key insights:
# 
# 1. GLOBAL CHECK: If total gas < total cost, it's impossible to complete
#    the circuit from ANY starting point. But if total gas >= total cost,
#    a solution MUST exist (guaranteed by problem constraints).
#
# 2. GREEDY SELECTION: If we start at station i and fail to reach station j
#    (run out of gas), then NO station between i and j-1 can be a valid start.
#    Why? Because we had EXTRA gas from station i when traveling i→j.
#    If we couldn't make it WITH extra gas, we definitely can't starting
#    from any station between i and j with LESS gas.
#    Therefore, our next candidate starting point must be j (or later).
#
# This allows us to find the answer in a single pass O(n) instead of
# trying every starting point O(n²).

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First, check if completing the circuit is even possible
        if sum(cost) > sum(gas):
            return -1 # Impossible: not enough total gas
        
        total = 0   # Current gas tank balance as we simulate the journey
        start = 0   # Our candidate starting station

        # Try to complete circuit starting from 'start'
        for i in range(len(gas)):
            # Calculate net gas at station i (gain - loss)
            total += gas[i] - cost[i]
            
            # If gas tank goes negative, we can't reach the next station
            if total < 0:
                # We failed starting from 'start', so reset everything
                total = 0      # Reset gas tank for new attempt
                start = i + 1  # Next station becomes our new candidate start
                # Note: All stations from old 'start' to 'i' are eliminated
        
        # If we reach here, we know a solution exists (from first check)
        # and 'start' is the valid starting station
        return start