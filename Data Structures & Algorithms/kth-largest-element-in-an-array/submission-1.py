from heapq import heapify, heappop
# Time: O(n + (n-k)log n) Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We will use a min heap
        heap = [num for num in nums]
        heapify(heap)

        # We pop the elements until the heap has k elements
        while len(heap) > k:
            heappop(heap)
        
        # Return heap[0], the smallest element in the heap
        return heap[0]