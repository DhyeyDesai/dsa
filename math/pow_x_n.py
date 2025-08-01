# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x==0: return 0
            if n == 0: return 1
            
            res = helper(x*x, n//2)
            return x*res if n%2 else res

        res = helper(x, abs(n))
        return res if n>=0 else 1/res



class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n == 0:
            return 1
        
        result = 1
        power = abs(n)

        while power:
            if power & 1:
                result*=x
            x*=x
            power>>=1

        
        return result if n>0 else 1/result




                