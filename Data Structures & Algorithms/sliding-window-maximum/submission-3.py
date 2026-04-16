class Solution:
    # Time: O(n), Spacew: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # In this solution, we are going to use a deque that stores indexes of the current window
        res = []
        q = deque()
        l = r = 0

        # 
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res