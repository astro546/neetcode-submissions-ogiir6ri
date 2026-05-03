from heapq import heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone) 
        
        new_stone = 0
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            new_stone = abs(x - y)
            if new_stone > 0: heappush(heap, -new_stone)

        if len(heap) == 1 and new_stone == 0:
            return -heap[0]
        elif not heap:
            return 0
        else:
            return new_stone
        
            