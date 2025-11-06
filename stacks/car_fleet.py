# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/description/

# INTUITION:
# 1. Cars closer to target arrive first (or form fleets). Process cars from closest to farthest.
# 2. A car catches up to form a fleet if its arrival time <= the car ahead's arrival time.
# 3. When cars form a fleet, they move at the slower car's speed, so we only track the slower one.
# 4. Use a stack to track independent fleets - each entry represents a fleet's arrival time.
#
# TIME COMPLEXITY: O(n log n) - due to sorting the cars by position
# SPACE COMPLEXITY: O(n) - for storing the pair array and stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        pair = [[p, s] for p,s in zip(position, speed)]
        
        stack = [] # Stack stores arrival times of each fleet

        # Sort by position and iterate from closest to target to farthest
        # [::-1] reverses to process cars starting from those nearest to target
        for p, s in sorted(pair)[::-1]:
            # Calculate time for current car to reach target
            stack.append((target - p)/s)

            # If current car catches up to the fleet ahead (arrives sooner or at same time),
            # they form one fleet, so remove current car (it merges with the one ahead)
            # stack[-1] is current car, stack[-2] is the car/fleet directly ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # Current car merges into fleet ahead
        
        # Number of independent fleets remaining
        return len(stack)
                