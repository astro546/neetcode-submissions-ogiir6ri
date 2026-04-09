class MinStack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return False

    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return False


    def getMin(self) -> int:
        if not self.isEmpty():
            return min(self.stack)
        else:
            return False
        
