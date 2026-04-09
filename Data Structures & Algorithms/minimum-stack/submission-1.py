class MinStack:
    # The getMin code takes O(1)
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
        
