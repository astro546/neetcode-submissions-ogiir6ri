from collections import Counter
from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m > n: return ""

        t_counter = Counter(t)
        window = Counter()
        counter = 0
        min_window_len = float('inf')
        res_coords = [-1, -1]
        
        inc_dec_cond = lambda x: s[x] in t_counter and window[s[x]] <= t_counter[s[x]]
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if inc_dec_cond(r):
                counter += 1

            while counter == m:
                window_len = r - l + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    res_coords = [l , r]

                if inc_dec_cond(l):
                    counter -= 1
                window[s[l]] -= 1
                l += 1

        return s[res_coords[0]:res_coords[1] + 1]
        