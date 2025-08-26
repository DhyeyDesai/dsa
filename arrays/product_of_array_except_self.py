# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

# Intuition:
# Handle zeros as special cases. Calculate the product of all non-zero elements.
# If there are 2+ zeros, all results are 0. If there's exactly 1 zero, only that 
# position gets the product (all others are 0). If no zeros, divide total product 
# by each element. Simple but requires division and careful zero handling.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        n = len(nums)

        # Calculate product of non-zero elements and count zeros
        for item in nums:
            if item == 0:
                zeros+=1
            else:
                product*=item
        
        # If 2 or more zeros, all products except self will be 0
        if zeros>1:
            return [0]*n
        
        result = [0] * n

        # Fill result array based on zero count
        for index, item in enumerate(nums):
            if zeros:
                # If there's exactly one zero
                if item==0:
                    # Only the zero position gets the product of all other elements
                    result[index] = product
                else:
                    # All non-zero positions get 0 (since one element is 0)
                    result[index] = 0
            else:
                # No zeros: divide total product by current element
                result[index] = product // item
            
        return result


# Intuition:
# Two-pass approach using prefix and postfix products. First pass fills each position 
# with the product of all elements to its left. Second pass (right to left) multiplies 
# each position by the product of all elements to its right. This avoids division 
# entirely and handles all cases naturally, including zeros.

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # First pass: calculate prefix products (product of all elements to the left)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # Store product of all elements before current index
            prefix *= nums[i]  # Update prefix to include current element
        
        # Second pass: multiply by postfix products (product of all elements to the right)
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply existing prefix by postfix
            postfix *= nums[i]  # Update postfix to include current element
        
        return res


                 

