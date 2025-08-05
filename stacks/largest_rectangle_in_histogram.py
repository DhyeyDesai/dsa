class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        currentStart = 0
        currentMinHeight = -1
        largestArea = 0
        for i, h in enumerate(heights):
            if h == 0:
                currentMinHeight = -1
                currentStart = -1
            else:
                if currentStart == 0:
                    currentStart = i
                
                currentMinHeight = min(currentMinHeight, h)
                currentArea = (i - currentStart + 1)*currentMinHeight
                largestArea  = max(currentArea, largestArea)
                print(currentArea, largestArea, currentMinHeight, currentStart)

        return largestArea