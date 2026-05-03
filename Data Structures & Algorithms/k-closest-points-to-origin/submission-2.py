from heapq import heapify, heappop
class Solution:
    # Time: O(n + k log n), Space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We only need the sum of the squares of x and y of all points to work.
        # Since in this solution we work with a max heap, we push negative values
        heap = [(-(point[0]**2 + point[1]**2), point) for point in points]
        heapify(heap)

        # We pop elements until the heap has only k elements
        # Each time we pop an element from the max heap, 
        # the next root of the heap will be smaller
        while len(heap) > k:
            heappop(heap)

        # Actually, since the max heap has k elements, all of this elements are
        # the k closest points to the center
        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res
        
