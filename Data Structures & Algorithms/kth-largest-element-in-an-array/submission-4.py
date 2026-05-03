from heapq import nlargest
# Time: O(k + (n-k)log n) Space: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # The previous submissions is the implementation of nlargest method
        return nlargest(k, nums)[-1]
        