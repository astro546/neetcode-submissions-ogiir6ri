class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            l_isalnum = s[l].isalnum()
            r_isalnum = s[r].isalnum()

            if l_isalnum and r_isalnum:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1

            elif not l_isalnum:
                l += 1
            elif not r_isalnum:
                r -= 1

        return True