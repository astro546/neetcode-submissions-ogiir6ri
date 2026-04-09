class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}
        current_op = ''
        stack = []
        i = 0
        res = 0
        for token in tokens:      
            if token not in operators:
                stack.append(int(token))

            else:
                r = stack.pop()
                l = stack.pop()
                print(token)
                if token == '+':
                    res = l + r
                elif token == '-':
                    res = l - r
                elif token == '*':
                    res = l * r
                elif token == '/':
                    res = int(l / r)
                stack.append(res)
            
        return stack.pop()


        