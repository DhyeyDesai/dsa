# 268. Missing Number
# https://neetcode.io/solutions/missing-number

# Solution 1 - Math
# Intuition:
# The array should contain numbers from 0 to n (where n = length of array).
# Using the arithmetic series formula, the sum of numbers from 0 to n is n*(n+1)/2.
# If we calculate this expected sum and subtract the actual sum of elements in the array,
# the difference will be the missing number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        ideal = n * (n + 1) //2
        return ideal - sum(nums)
    
# Solution 2 - XOR (Bit Manipulation)
# Intuition:
# XOR has two key properties that make this work:
# 1. a ^ a = 0 (any number XORed with itself equals 0)
# 2. a ^ 0 = a (any number XORed with 0 equals itself)
# 3. XOR is commutative: a ^ b ^ c = c ^ b ^ a (order doesn't matter)
#
# Strategy: XOR all numbers from 0 to n, then XOR all numbers in the array.
# All numbers that appear will cancel out (become 0), leaving only the missing number.
#
# Example: nums = [3,0,1] (missing 2)
# - XOR all indices and n: 0 ^ 1 ^ 2 ^ 3 = 0
# - XOR all array elements: 3 ^ 0 ^ 1 = 2
# - Combine them: (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)
#                = 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 3 ^ 3
#                = 0 ^ 0 ^ 0 ^ 2  (pairs cancel out)
#                = 2 (the missing number!)

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result
