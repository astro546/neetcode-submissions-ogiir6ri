from heapq import heappush, heappop
from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1 or n == 1: return nums

        res = []
        max_heap = []
        window = Counter()
        for r in range(k):
            heappush(max_heap, -nums[r])
            window[nums[r]] += 1 
        res.append(-max_heap[0])

        l = 0
        for r in range(k, n):
            heappush(max_heap, -nums[r])
            window[nums[r]] += 1

            window[nums[l]] -= 1
            l += 1

            while max_heap and window[-max_heap[0]] == 0:
                heappop(max_heap)
            
            res.append(-max_heap[0])

        return res