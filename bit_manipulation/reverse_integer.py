# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

# INTUITION:
# ----------
# Reverse an integer by extracting digits from right to left and building
# the reversed number. The key challenge is detecting overflow BEFORE it 
# happens (since we can't use 64-bit integers to check after).

# Think of it like peeling digits off the end of a number and stacking them
# in reverse order, but stop if the stack would grow too large (overflow).

# APPROACH:
# ---------
# 1. Extract the rightmost digit using modulo (%)
# 2. Remove the rightmost digit using division (/)
# 3. Check if adding this digit to our result would cause overflow
# 4. If safe, append digit to result by: result = result * 10 + digit
# 5. Repeat until no digits remain

# TIME COMPLEXITY: O(log x) - we process each digit once, and x has log₁₀(x) digits
# SPACE COMPLEXITY: O(1) - only using a few variables regardless of input size


import math

class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit signed integer boundaries
        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        res = 0
        
        # Continue while there are digits to process
        while x:
            # Extract the last digit (handles negative via fmod)
            # fmod(-123, 10) = -3 (keeps sign of dividend)
            digit = int(math.fmod(x, 10))
            
            # Remove the last digit from x
            # int(-123 / 10) = -12 (truncates toward zero)
            x = int(x / 10)

            # OVERFLOW CHECK (positive): Will res * 10 + digit exceed MAX?
            # If res > 214748364, then res * 10 will overflow
            # If res == 214748364 and digit > 7, then res * 10 + digit overflows
            if res > (MAX // 10) or (res == (MAX // 10) and digit > (MAX % 10)):
                return 0
            
            # OVERFLOW CHECK (negative): Will res * 10 + digit go below MIN?
            # If res < -214748364, then res * 10 will underflow
            # If res == -214748364 and digit < -8, then res * 10 + digit underflows
            if res < (MIN // 10) or (res == (MIN // 10) and digit < (MIN % 10)):
                return 0
            
            # Safe to add: shift result left by one digit and append new digit
            # Example: res=12, digit=3 → res = 12*10 + 3 = 123
            res = (res * 10) + digit

        return res

