from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l<=r:
            m = l+(r-l)//2
            totalTime = 0

            for p in piles:
                totalTime += ceil(p/m)
            
            if totalTime<=h:
                result = m
                r = m-1
            else:
                l = m+1
        
        return result

                