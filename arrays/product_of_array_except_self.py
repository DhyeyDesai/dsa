# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        n = len(nums)

        for item in nums:
            if item == 0:
                zeros+=1
            else:
                product*=item
        
        if zeros>1:
            return [0]*n
        
        result = [0] * n
        
        for index, item in enumerate(nums):
            if zeros:
                if item==0:
                    result[index] = product
                else:
                    result[index] = 0
            else:
                result[index] = product // item
            
        return result


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix *=nums[i]
        
        return res


                 

