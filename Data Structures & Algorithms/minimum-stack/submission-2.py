class MinStack:
    # The getMin code takes O(1)
    # The stack does not store the values themselves, but stores encoded values
    # The way to encode the values is: val - min (dif)
    # If at the time when you push a new val in the stack, val - min < 0, that means that val is the new min
    #   so, min = val
    # When you pop an element, if pop < 0, that means that pop was the min, so, update the min:
    #   min = min - pop
    # Finally, to get the top element, if top < 0, that means top = min, else, calculate:
    #   top = top + min
    def __init__(self):
        self.stack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minValue = val
        else:
            dif = val - self.minValue
            self.stack.append(dif)
            if dif < 0: 
                self.minValue = val

    def pop(self) -> None:
        if not self.stack:
            return 

        pop = self.stack.pop()
        if pop < 0:
            self.minValue = self.minValue - pop
         

    def top(self) -> int:
        if not self.stack:
            return 
            
        top = self.stack[-1]
        if top > 0:
            return top + self.minValue
        else: 
            return self.minValue
        

    def getMin(self) -> int:
        return self.minValue
        
