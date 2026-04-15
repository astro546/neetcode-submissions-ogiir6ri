from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m: return False

        s1_counter = Counter(s1)
        window = Counter()
        counter = 0
        for r in range(n):
            if s2[r] in s1_counter:
                window[s2[r]] += 1
                if window[s2[r]] <= s1_counter[s2[r]]:
                    counter += 1
        if counter == n: return True

        l = 0
        for r in range(n,m):
            if s2[r] in s1_counter:
                window[s2[r]] += 1
                if window[s2[r]] <= s1_counter[s2[r]]:
                    counter += 1

            if s2[l] in s1_counter:
                if window[s2[l]] <= s1_counter[s2[l]]:
                    counter -= 1
                window[s2[l]] -= 1
            l += 1
            if counter == n: return True
        return False
            

            


            

        
        

        
        