class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_hash = set(['[', '(', '{'])
        right_hash = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        for char in s:
            if char in left_hash:
                stack.append(char)
            elif stack and stack[-1] == right_hash[char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0