# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/description/

# TODO: Understand the bit concepts behind this in depth
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
    
        while b != 0:
            # Calculate sum without carry
            sum_without_carry = (a ^ b) & mask
            
            # Calculate carry
            carry = ((a & b) << 1) & mask
            
            # Update a and b
            a = sum_without_carry
            b = carry
        
        # Handle negative numbers (if a is negative in 32-bit)
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
        
        return a
    