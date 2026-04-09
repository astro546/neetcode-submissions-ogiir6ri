class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_container = 0
        while l < r:
            height_l, height_r = heights[l], heights[r]
            width = r - l 
            area = min(height_l, height_r) * width
            max_container = max(max_container, area)

            if height_l > height_r:
                r -= 1
            else:
                l += 1

        return max_container
        