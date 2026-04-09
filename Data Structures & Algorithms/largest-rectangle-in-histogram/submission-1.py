class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]

        maxArea = 0
        for idx, h in enumerate(heights):
            
            l = idx
            while l >= 0 and heights[l] >= h:
                l -= 1

            r = idx
            while r < len(heights) and heights[r] >= h:
                r += 1

            width = r - l - 1
            area = width * h
            maxArea = max(maxArea, area) 
        return maxArea
