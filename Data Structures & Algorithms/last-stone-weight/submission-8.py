from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since we need to get the two heaviest stones of the list,
        # we need to use a max heap, and to create a max heap,
        # we need to push the negative versions of each stone
        heap = [-stone for stone in stones]
        heapify(heap)

        # We pop two elements from the heap,
        # and only push a new element if abs(x-y) > 0
        new_stone = 0
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            if abs(x-y) > 0: heappush(heap, -abs(x-y))
        
        # Finally, we return the remaining element from the heap if exists,
        # else, return 0
        return -heap[0] if heap else 0

           