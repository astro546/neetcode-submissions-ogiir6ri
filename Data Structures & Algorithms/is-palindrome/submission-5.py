class Solution:
    # Time: O(n), Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        # We define l and r pointers. These pointers moves in opposite directions
        l, r = 0, len(s) - 1

        # In each iteration, until l >= r
        # 1.- First, we check if both s[l] and s[r] are alphanumeric characters
        #   If this condition is met, then we check if the lowercase version of both are different,
        #   if both lowercase versions are diferente, that means s in not a palindrome, so, return False
        #   else, we can continue checking the string.
        while l < r:
            l_isalnum = s[l].isalnum()
            r_isalnum = s[r].isalnum()

            if l_isalnum and r_isalnum:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1

            # 2.- Else, check if either s[l] or s[r] is not alphanumeric, 
            #   and, move the respective pointer to match the next alphanumeric character
            elif not l_isalnum:
                l += 1
            elif not r_isalnum:
                r -= 1

        return True


        # isalnum can define as:
        # def alphaNum(self, c):
        # return (ord('A') <= ord(c) <= ord('Z') or
        #        ord('a') <= ord(c) <= ord('z') or
        #        ord('0') <= ord(c) <= ord('9'))