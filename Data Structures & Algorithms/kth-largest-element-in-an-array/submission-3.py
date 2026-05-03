from heapq import heapify, heappushpop
# Time: O(k + (n-k)log n) Space: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We will use the first k elements to build the first version of the min heap
        heap = nums[:k]
        heapify(heap)

        # For each number in nums, if the current number is greater than
        # the smallest number in the min heap, push the new number and pop the root
        # Since we push the new number and pop the root, we always keep the same length
        # that is k
        for num in nums[k:]:
            if num > heap[0]:
                heappushpop(heap, num)

        # return the smallest element
        return heap[0]

        