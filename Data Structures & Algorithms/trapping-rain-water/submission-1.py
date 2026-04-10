class Solution:
    # Time: O(n), Space: O(1)
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        # We use 2 pointers moving in opposite directions,
        # and track the current maximum height in both sides
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r];
        res = 0
        while l < r:
            # We move the pointer that has the current smallest height,
            # update their maximum, and add to the res
            # the difference between the current maximum and the current height. 
            # This difference tell us for each bar, how much water are between the maximum height and the current bar
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        