from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(point[0]**2 + point[1]**2, point) for point in points]
        heapify(heap)
        
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res
