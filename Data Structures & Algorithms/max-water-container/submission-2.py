class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_container = 0
        while l < r:
            width = r - l 
            area = min(heights[l], heights[r]) * width
            max_container = max(max_container, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_container
        