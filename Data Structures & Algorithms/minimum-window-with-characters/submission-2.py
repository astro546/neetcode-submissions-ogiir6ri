from collections import Counter
from collections import deque
class Solution:
    # Time: O(m + n), Space: O(m), n = len(s), m = number of unique characters in the string t and s
    def minWindow(self, s: str, t: str) -> str:
        # If t is greater than s, we cannot work in s, so, return False
        n, m = len(s), len(t)
        if m > n: return ""

        # We use hashmaps for track requencies in t and the current window,
        # also, we have to use a counter to count if the current window has the same amount
        # of characters than t.
        # We need to track the minimum length of widows,
        # and the left and right coordinates for the current window.
        # We area going to track the coordinates, beacuse the problems asks for the substring,
        # not for a minimum or maximum number.
        t_counter = Counter(t)
        window = Counter()
        counter = 0
        min_window_len = float('inf')
        res_coords = [-1, -1]
        
        # inc_dec_cond is a function that get the condition to check if we increment or decrement counter.
        # This condiction checks if s[x] is in t_counter and if there are not remaining characters
        # that can we use in the future.
        inc_dec_cond = lambda x: s[x] in t_counter and window[s[x]] <= t_counter[s[x]]
        l = 0
        for r in range(n):
            # First, increment the respective frequenciy of s[r]
            window[s[r]] += 1
            if inc_dec_cond(r):
                counter += 1

            # We expand the window until counter == m,
            # And we shrink the window until counter < m
            while counter == m:
                # If the current window is smaller than the current min window,
                # update the min window len and the final coordinates
                window_len = r - l + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    res_coords = [l , r]

                # Before remove the left element and increment l, we decrement the counter
                if inc_dec_cond(l):
                    counter -= 1
                window[s[l]] -= 1
                l += 1

        return s[res_coords[0]:res_coords[1] + 1]
        