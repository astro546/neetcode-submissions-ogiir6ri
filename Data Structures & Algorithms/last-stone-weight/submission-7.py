from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        new_stone = 0
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            
            if abs(x-y) > 0: heappush(heap, -abs(x-y))
        return -heap[0] if heap else 0

           