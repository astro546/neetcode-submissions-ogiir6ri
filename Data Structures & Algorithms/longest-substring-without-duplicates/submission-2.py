class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        unique_chars = set()
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            current_len = r - l + 1
            unique_chars.add(s[r])
            max_len = max(max_len, current_len)
        return max_len