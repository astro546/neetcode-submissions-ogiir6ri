class Solution:
    # Time: O(n), Space: O(1)
    def maxArea(self, heights: List[int]) -> int:
        # We use two pointers moving in opposite directions
        l, r = 0, len(heights) - 1
        max_container = 0
        while l < r:
            # In each iterations, calculate the area and update the max container
            width = r - l 
            area = min(heights[l], heights[r]) * width
            max_container = max(max_container, area)

            # Move the pointer that has the minimum height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_container
        