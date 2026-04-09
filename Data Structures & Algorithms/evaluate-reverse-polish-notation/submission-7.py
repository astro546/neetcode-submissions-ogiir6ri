class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)
        # This solution does not verify if tokens[i] is a operator by searching it in a set.
        # In place of that, we verify if tokesn[i] is an operator if a direct if-else sentence
        # and each case, we perform the operation and push the result in the stack.
        # The last case is when tokens[i] is a number, so push the number in the stack
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
        