# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

"""
Solution 1 Intuition (Floyd's Cycle Detection):
A number is either happy (eventually reaches 1) or gets stuck in a cycle of non-1 values.
We can use Floyd's cycle detection algorithm here! Treat the sum-of-squares operation
as following a linked list where each number points to its sum-of-squares. If there's 
a cycle and it doesn't contain 1, the number is unhappy. If we reach 1, it's happy.
This approach uses O(1) space compared to the set-based solution.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Use Floyd's cycle detection (tortoise and hare)
        slow = n
        fast = self.sumOfSquares(n)  # Fast starts one step ahead

        # Continue until slow and fast meet (cycle detected)
        while slow != fast:
            # Fast pointer moves 2 steps
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            # Slow pointer moves 1 step
            slow = self.sumOfSquares(slow)

        # If the cycle contains 1, the number is happy
        if fast == 1:
            return True
        return False

    def sumOfSquares(self, n):
        """Calculate sum of squares of digits in n"""
        output = 0

        while n:
            digit = n % 10          # Get rightmost digit
            digit = digit ** 2      # Square it
            output += digit         # Add to sum
            n = n // 10            # Remove rightmost digit
        
        return output


"""
Solution 2 Intuition (Hash Set):
More straightforward approach - keep track of all numbers we've seen. If we see
a number again, we're in a cycle. If we reach 1 before seeing a repeat, it's happy.
This uses O(k) space where k is the length of the cycle, but is easier to understand.
"""

class Solution2:
    def isHappy(self, n: int) -> bool:
        visited = set()  # Track numbers we've already seen

        # Continue until we find a cycle (revisit a number)
        while n not in visited:
            visited.add(n)                    # Mark current number as visited
            n = self.sumOfSquares(n)          # Move to next number in sequence

            # If we reach 1, the original number is happy
            if n == 1:
                return True
        
        # If we exit the loop, we found a cycle that doesn't contain 1
        return False
    
    def sumOfSquares(self, n):
        """Calculate sum of squares of digits in n"""
        output = 0

        while n:
            digit = n % 10          # Extract rightmost digit
            digit = digit ** 2      # Square the digit
            output += digit         # Add to running sum
            n = n // 10            # Remove the processed digit
        
        return output