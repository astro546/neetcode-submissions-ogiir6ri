class Solution:
    # This version was written completely by me without copypasting
    # For each temp in the temperatures array, before pushing it into the stack (index, temp),
    # Verify if temperatures[i] is warmer than the top of the stack.
    # If this condition is true, pop the elements until the stack lefts empty, or
    # the top element was warmer than temperatures[i].
    # For each popped element, calculate the difference of the days by: i - tempArrIdx
    # and store it in res[tempArrIdx]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                tempArrIdx, stackTemp = stack.pop()
                res[tempArrIdx] = i - tempArrIdx
            stack.append((i, t))
        return res