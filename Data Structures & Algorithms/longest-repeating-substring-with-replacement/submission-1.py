from collections import Counter
class Solution:
    # Time: O(n), Space: O(m), n = len(s), m = number of unique chars in s
    def characterReplacement(self, s: str, k: int) -> int:
        # We use a hash map for count the frequencies of the characters,
        # And also, we track the max frequencie of the current window,
        # and the max length of a window registered
        l = 0
        max_len, max_f = 0, 0
        char_counter = Counter()
        for r in range(len(s)):
            # Add the right char and update the max frequencie
            char_counter[s[r]] += 1
            max_f = max(max_f, char_counter[s[r]])

            # if the difference between the length of the current window and the current max frequencie
            # is greater than k, that means, we cant replace k character to left a string 
            # with only one character distinct, or, in other words, in this condition,
            # there must be at least 2 distinct characters in the string.
            # In this case, shirnk the window by the left
            while not((r - l + 1) - max_f <= k):
                char_counter[s[l]] -= 1
                l += 1
            
            # Finally, update the max length of a window founded
            max_len = max(max_len, (r - l + 1))
        return max_len