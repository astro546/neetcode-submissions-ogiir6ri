class Solution:
    # Time: O(n), Spacew: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # In this solution, we are going to use a deque that stores indexes of the current window
        res = []
        q = deque()
        l = r = 0

        # For each iteration of r
        for r in range(len(nums)):
            # First, we have to remove all numbers from the right 
            # that are smaller than the new right number,
            # and then, add the new number.
            # Doing this, cause the queue l
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Since the queue is sorted letting the max number in the left,
            # and the min number in the right,
            # if the max number is outside of the window, pop their index from the left
            if l > q[0]:
                q.popleft()
            
            # We start pushing the maximum of each window since we already created our first window
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res