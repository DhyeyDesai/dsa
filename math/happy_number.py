class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)

            
        if fast == 1:
            return True
        return False

    
    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n%10
            digit = digit ** 2
            output+=digit

            n=n//10
        
        return output


class Solution2:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False
    
    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n%10
            digit = digit ** 2
            output+=digit

            n=n//10
        
        return output
