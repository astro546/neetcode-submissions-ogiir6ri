class Solution:
    # O(n log n) because the sort function
    # First, pair the speeds with the position of each car*
    # Then, sort the pairs, and iterate the array of pairs
    # For each pair:
    #   - Calculate the time
    #   - If the stack is not empty, and the time at the top of the stack is greater or equal than the current time, 
    #       continue, that means that the current time is part of the car fleet of the time at the top of the stack
    #   - Else, append the time to the stack
    # The number of car fleets at the target is the number of elements in the stack, so, return len(stack)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        
        for p, s in pair:
            time = (target - p)/s
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)
        

        
        