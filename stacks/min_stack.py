# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/

# Intuition:
# We need a stack that supports push, pop, top, and retrieving the minimum element in O(1).
# Instead of storing the actual values, we store the difference between the pushed value and the current minimum.
# This way, we can track how the minimum changes without using an extra stack.

class MinStack:

    def __init__(self):
        self.min = float("inf")  # Current minimum element
        self.stack = []          # Stack stores differences (val - min)

    def push(self, val: int) -> None:
        if not self.stack:
            # First element: store 0 difference, set min to val
            self.stack.append(0)
            self.min = val
        else:
            # Store the difference
            self.stack.append(val - self.min)
            # If new value is smaller, update min
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        
        # If popped value was negative, it means the min was updated at that push.
        # Restore the previous min.
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        if not self.stack:
            return

        top = self.stack[-1]
        # If top is negative, the actual value is the current min
        if top < 0:
            return self.min
        else:
            # Otherwise, reconstruct the value using min + difference
            return self.min + top

    def getMin(self) -> int:
        # Return current minimum
        return self.min


# Usage Example:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()