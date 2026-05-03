from heapq import heapify, heappushpop
# Time: O(n + (n-k)log n) Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We will use the first k elements to build the first version of the min heap
        heap = nums[:k]
        heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heappushpop(heap, num)

        return heap[0]

        