# 136. Single Number
# https://leetcode.com/problems/single-number/description/

# INTUITION:
# 1. Use XOR operation's special properties to find the unique element
# 2. Key properties of XOR:
#    - a ^ a = 0 (any number XOR itself equals 0)
#    - a ^ 0 = a (any number XOR 0 equals the number itself)
#    - XOR is commutative and associative (order doesn't matter)
# 3. When we XOR all numbers, pairs cancel out (become 0), leaving only the single number

# EXAMPLE:
# nums = [2, 2, 1]
# Step by step: 0 ^ 2 ^ 2 ^ 1 = ((0 ^ 2) ^ 2) ^ 1 = (2 ^ 2) ^ 1 = 0 ^ 1 = 1

# BRILLIANT INSIGHT: 
# - All duplicate numbers XOR to 0
# - The single number XOR 0 = the single number
# - Time: O(n), Space: O(1) - no extra data structures needed!

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # Initialize result (0 is XOR identity: any number ^ 0 = that number)
        
        for n in nums:
            # XOR current number with running result
            # Pairs of identical numbers will cancel out (become 0)
            # The single number will remain since it has no pair to cancel with
            res = n ^ res
            
        # After processing all numbers, res contains the single number
        return res