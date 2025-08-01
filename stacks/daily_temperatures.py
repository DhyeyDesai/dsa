class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, num in enumerate(temperatures):
            while len(stack) and num>stack[-1][0]:
                stackNum, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
 
            stack.append((num, i))


        return result


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            while len(stack) and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            stack.append(i)
            if len(stack) > 1:
                result[i] = stack[-2] - stack[-1]
        return result

