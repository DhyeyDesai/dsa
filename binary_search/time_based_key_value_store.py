# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values)-1

        while l<=r:
            m = l+(r-l)//2

            if values[m][1]<timestamp:
                res = values[m][0]
                l = m+1
            elif values[m][1]==timestamp:
                return values[m][0]
            else:
                r = m-1
        
        return res
