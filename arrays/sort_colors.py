# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

# Sort an array of 0's 1's and 2's


class Solution:
    def sortColors(self, nums: List[int]) -> None:
       l = m = 0
       r = len(nums) - 1
       while m<=r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m+=1
                l+=1
            elif nums[m] == 1:
                m+=1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r-=1
               
               
            
