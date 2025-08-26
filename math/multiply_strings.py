# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/description/

"""
Intuition:
Simulate elementary school multiplication! The key insight is that when multiplying
digit at position i in num1 with digit at position j in num2, the result contributes
to positions i+j and i+j+1 in the final answer (due to potential carry).

Process:
1. Create result array of size len(num1) + len(num2) (max possible length)
2. Reverse both strings to process from least significant digit
3. For each digit pair, multiply and add to appropriate positions
4. Handle carries by propagating overflow to next position
5. Remove leading zeros and convert back to string

The beauty is that we handle carries as we go, avoiding complex carry propagation later.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge case: if either number is "0", result is "0"
        if "0" in [num1, num2]:
            return "0"
        
        # Create result array with maximum possible length
        # Product of m-digit and n-digit numbers has at most m+n digits
        res = [0] * (len(num1) + len(num2))

        # Reverse both strings to process from least significant digit (rightmost)
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply each digit of num1 with each digit of num2
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # Multiply current digits
                digit = int(num1[i1]) * int(num2[i2])
                
                # Add the product to the appropriate position
                res[i1 + i2] += digit
                
                # Handle carry: move tens digit to next position
                res[i1 + i2 + 1] += res[i1 + i2] // 10  # Carry
                res[i1 + i2] %= 10                       # Keep only units digit

        # Reverse result array to get most significant digit first
        res = res[::-1]
        
        # Remove leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        # Convert remaining digits to strings and join
        res = map(str, res[beg:])
        return "".join(res)