# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

"""
Solution 1 Intuition (Recursive - Exponentiation by Squaring):
The key insight is that x^n can be computed efficiently using the property:
- If n is even: x^n = (x^2)^(n/2)
- If n is odd: x^n = x * (x^2)^(n/2)

This reduces the problem size by half each time, achieving O(log n) complexity.
For negative exponents, we compute x^|n| and take the reciprocal.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # Base cases
            if x == 0: return 0  # 0^n = 0 (for n > 0)
            if n == 0: return 1  # x^0 = 1 (for any x ≠ 0)
            
            # Recursive case: reduce problem by half
            # Calculate (x^2)^(n//2) instead of x^n directly
            res = helper(x * x, n // 2)
            
            # If n is odd, multiply by an extra x
            return x * res if n % 2 else res

        # Handle negative exponents
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


"""
Solution 2 Intuition (Iterative - Binary Exponentiation):
Same mathematical principle but implemented iteratively using bit manipulation.
We build the result by examining each bit of the exponent from right to left.
For each bit position, we decide whether to include the current power of x.

Think of n in binary: if n = 13 = 1101₂, then x^13 = x^8 * x^4 * x^1
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle base cases
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = 1
        power = abs(n)  # Work with positive exponent, handle sign at the end

        # Iterate through each bit of the exponent
        while power:
            # If current bit is 1, multiply result by current power of x
            if power & 1:  # Check if least significant bit is 1
                result *= x
            
            # Square x for the next bit position
            x *= x
            
            # Right shift to process the next bit
            power >>= 1

        # Handle negative exponents by taking reciprocal
        return result if n > 0 else 1 / result