from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num for num in nums]
        heapify(heap)

        while len(heap) > k:
            heappop(heap)
        
        return heap[0]