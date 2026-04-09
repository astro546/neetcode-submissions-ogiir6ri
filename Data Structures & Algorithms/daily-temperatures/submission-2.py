class Solution:
    # O(n)
    # First, create the output array and the stack
    # Then iterates, the temperatures array by enumerate them to work with the index and the value in the same time
    # For each iteration:
    #   -While the stack is not empty and the current temperature is greater than the top of the stack:
    #       - Pop the top element of the stack
    #       - subtract the stack index to the index of the temperature, and store it in res[stack index] 
    #   - Once the while loop finishes, push the current temperature and its index in the stack
    # return res
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

        