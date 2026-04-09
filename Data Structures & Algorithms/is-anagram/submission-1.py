class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sum = 0
        for i in range(len(s)):
            sum += (ord(s[i]) - ord('a')) * ord(s[i])
            sum -= (ord(t[i]) - ord('a')) * ord(t[i])
        
        return sum == 0
        