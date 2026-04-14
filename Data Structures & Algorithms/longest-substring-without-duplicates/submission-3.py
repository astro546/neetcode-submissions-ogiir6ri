class Solution:
    # Time: O(N), Space: O(min(N,M)) where N= len(s), M= len(character set)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a set to track the unique chars in the current window
        max_len = 0
        l = 0
        unique_chars = set()
        # In each iteration, if s[r] is in unique chars, we have a repeated char,
        # so, move s until s[r] will removed
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            # then, update the length of the window, add the new char in the set and update the max len
            current_len = r - l + 1
            unique_chars.add(s[r])
            max_len = max(max_len, current_len)
        return max_len