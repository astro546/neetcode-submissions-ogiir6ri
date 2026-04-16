from heapq import heappush, heappop
from collections import Counter
class Solution:
    # Time: O(n log n), Space: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # If numsd has only 1 number, or k = 1,
        # That means, every number is the maximum of their respective window,
        # so, nums does not change, due to this, return nums
        n = len(nums)
        if k == 1 or n == 1: return nums

        # We use a max heap to track the max number in the current window,
        # and a hash map for window to track the frequencies of each number
        res = []
        max_heap = []
        window = Counter()

        # We create and process the first window
        for r in range(k):
            heappush(max_heap, -nums[r])
            window[nums[r]] += 1 
        res.append(-max_heap[0])

        l = 0
        for r in range(k, n):
            # For the following windows, first, we push the right elemnt into the max heap
            # and update their frequencie in window
            heappush(max_heap, -nums[r])
            window[nums[r]] += 1

            # Then, we move l and decrement its frequencie in window
            window[nums[l]] -= 1
            l += 1

            # Finally, we have to remove the roots that are no longer into the current window
            while max_heap and window[-max_heap[0]] == 0:
                heappop(max_heap)
            
            res.append(-max_heap[0])

        return res