class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)
        # In this code, we iterate the array, in each step:
        # Verify if the token is a number or is a operator.
        # If is a number, push it to the stack like an integer
        # If is a operator, pop the 2 elements of the stack:
        #   The first element is the right operator.
        #   The last element is the left operator.
        # Do the respective operation in function of the operator
        # Push the result of the operation
        # When the for loop finishes, the result will be the only element in the stack, so return stack.pop()
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


        