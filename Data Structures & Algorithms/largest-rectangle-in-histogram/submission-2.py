class Solution:
    # O(n^2)
    # In this solution, we iterate the height array.
    # For each h in height:
    #   - Move the left index to the left until a short bar than the current bar is found
    #   - Move the right index to the right until a short bar than the current bar is found
    #   - Calculate thw width: right - left - 1
    #   - Calculate the area: width * current height
    #   - if area > maxArea, maxArea = area
    # return maxArea
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
