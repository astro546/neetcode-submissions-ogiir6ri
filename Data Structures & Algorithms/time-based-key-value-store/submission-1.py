class TimeMap:

    def __init__(self):
        self.maps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.maps.get(key): 
            self.maps[key] = []
        self.maps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timeMap = self.maps.get(key, [])

        l, r = 0, len(timeMap) - 1
        recentValue = ""
        while l <= r:
            m = l + (r - l) // 2
            if timeMap[m][1] > timestamp:
                r = m - 1
            else:
                recentValue = timeMap[m][0]
                l = m + 1
        print('recentValue: ', recentValue)
        return recentValue
