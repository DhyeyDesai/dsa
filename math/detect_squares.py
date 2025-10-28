# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares/description/


# Intuition (Approach 1):
# This solution uses a brute force approach with a single hash map to store all points and their frequencies.

# 1. Store all added points as (x,y) tuples with their frequencies in a dictionary
# 2. For count(): iterate through ALL stored points to find potential diagonal corners
# 3. A point (x,y) is diagonal to query (px,py) if |x-px| = |y-py| and they form a valid square
# 4. Multiply frequencies of the diagonal corner and the two other required corners

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        # Store point frequencies using tuple as key: (x,y) -> count
        self.pointsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # Convert list to tuple for hashable key and increment frequency
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        
        # Iterate through all stored points to find potential diagonal corners
        for (x, y), freq in self.pointsCount.items():
            # Check if current point can be diagonal corner:
            # 1. Same distance in x and y directions (square property)
            # 2. Not the same point (x != px)
            if abs(x - px) == abs(y - py) and x != px:
                # If (x,y) is diagonal to (px,py), other corners are (x,py) and (px,y)
                # Multiply frequencies: diagonal_corner * corner1 * corner2
                res += freq * self.pointsCount.get((x, py), 0) * self.pointsCount.get((px, y), 0)
        
        return res
    

# Intuition (Approach 2):
# This solution optimizes by organizing points in a nested dictionary structure grouped by y-coordinates.

# 1. Store points as pointsCount[y][x] = frequency, grouping by rows
# 2. For count(): only check points in the same row as query point as potential adjacent corners
# 3. Calculate side length from query to adjacent corner, then check if other corners exist at calculated positions
# 4. This reduces search space by avoiding iteration through all points

class DetectSquares2:

    def __init__(self):
        # Nested dictionary: y_coordinate -> {x_coordinate -> frequency}
        # This groups points by rows, reducing search space
        self.pointsCount = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        # Group by y-coordinate first, then store x-coordinate frequency
        self.pointsCount[y][x] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        
        # Early return if no points exist at the same y-level as query point
        if py not in self.pointsCount:
            return 0
            
        res = 0
        # Get all points in the same row as query point
        row = self.pointsCount[py]
        
        # For each point in the same row (potential corner of square)
        for x, freq in row.items():
            # Skip the query point itself
            if x == px:
                continue
                
            # Calculate side length of potential square
            d = x - px
            
            # The other two corners must be at (px, py±d) and (x, py±d)
            # Check both possible y-coordinates: py+d and py-d
            for ny in (py + d, py - d):
                if ny in self.pointsCount:
                    # Multiply frequencies of all three other corners:
                    # - freq: frequency of (x, py) - corner in same row
                    # - self.pointsCount[ny][px]: frequency of (px, ny) - corner above/below query
                    # - self.pointsCount[ny][x]: frequency of (x, ny) - diagonal corner
                    res += freq * self.pointsCount[ny][px] * self.pointsCount[ny][x]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)