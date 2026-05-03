from heapq import heapify, heappop
class Solution:
    # Time: O(n + k log n), Space: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We only need the sum of the squares of x and y of all points to work.
        heap = [(-(point[0]**2 + point[1]**2), point) for point in points]
        heapify(heap)

        while len(heap) > k:
            heappop(heap)

        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res
        
