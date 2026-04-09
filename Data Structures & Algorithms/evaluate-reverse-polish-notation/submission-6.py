class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                r, l = stack.pop(), stack.pop()
                stack.append(int(l / r))
            else:
                stack.append(int(token))
            
        return stack.pop()
        