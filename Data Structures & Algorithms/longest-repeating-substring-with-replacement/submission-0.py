from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len, max_f = 0, 0
        char_counter = Counter()
        for r in range(len(s)):
            char_counter[s[r]] += 1
            max_f = max(max_f, char_counter[s[r]])
            while not((r - l + 1) - max_f <= k):
                char_counter[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r - l + 1))
        return max_len