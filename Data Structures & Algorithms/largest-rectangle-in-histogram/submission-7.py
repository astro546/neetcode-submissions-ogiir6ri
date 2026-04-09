class Solution:
    # O(n)
    # This solution uses a stack to track the nearest bar that is shortest than the current bar
    # We perform one iteration to fill the leftMost array with the indexes of the leftmost shortest bar
    # and one for the rightMost array. 
    # Then, iterates the leftMost and rightMost arrays at the same time to calculate the areas of the rectangles
    # and calculate the maximum area
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea

        