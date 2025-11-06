# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# INTUITION:
# 1. For each bar, we need to find how far it can extend left and right (until hitting shorter bars)
# 2. Use a monotonic increasing stack to track bars that can potentially extend further
# 3. When we hit a shorter bar, pop taller bars and calculate their max area (they're blocked now)
# 4. The stack stores indices, allowing us to calculate width when we find boundaries
#
# TIME COMPLEXITY: O(n) - each bar is pushed and popped from stack at most once
# SPACE COMPLEXITY: O(n) - stack can hold up to n bars in worst case (increasing heights)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Stack stores (index, height) pairs in increasing height order

        for i, h in enumerate(heights):
            start = i # Track where the current height could have started
            
            # Pop all bars taller than current height (they can't extend past here)
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                
                # Calculate area: height × width
                # Width = current index - where that bar started
                maxArea = max(maxArea, height * (i-index))

                # Current bar can extend back to where the popped bar started
                # (since current bar is shorter, it could've started there too)
                start = index

            # Push current bar with its potential starting position
            stack.append((start, h))

        # Process remaining bars in stack (they extend to the end)
        for i, h in stack:
            # These bars can extend all the way to the end
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea