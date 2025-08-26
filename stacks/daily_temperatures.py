# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# Intuition:
# For each day, we want to know how many days we must wait until a warmer temperature.
# This is a "next greater element" type problem, which can be solved efficiently with a stack.
# We use a monotonic stack to keep track of indices (or values+indices) of days with unresolved temperatures.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)   # Default 0 for days with no warmer future temp
        stack = []  # Monotonic decreasing stack: stores (temperature, index)
        
        # Traverse from left to right
        for i, num in enumerate(temperatures):
            # If current temp is warmer than the last unresolved one, resolve it
            while len(stack) and num > stack[-1][0]:
                stackNum, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx  # Days waited until warmer temperature
            
            # Push current day onto stack
            stack.append((num, i))

        return result


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack holds indices of days, maintaining decreasing temperatures
        
        # Traverse from right to left
        for i in range(n-1, -1, -1):
            # Pop all smaller/equal temps since they can't be the "next warmer day"
            while len(stack) and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            # If stack not empty, the top is the next warmer day
            if stack:
                result[i] = stack[-1] - i
            
            # Push current index to stack
            stack.append(i)
        
        return result
