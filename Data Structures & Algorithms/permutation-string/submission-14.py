from collections import Counter
class Solution:
    # This version was written by my own whitout copypasting
    # Time: O(n), Space: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If n > m, that means, the test string is greater than the string that will be tested,
        # so, is imposible to get a permutation in s2, so , return False
        n, m = len(s1), len(s2)
        if n > m: return False

        # In this solution, we are going to use two hashmap,
        # One like a counter for s1,
        # and another like a counter for the current window to track frequencies for each char.
        # Also, we will need a counter variable to track if we have the same aumnt of characters than s1
        s1_counter = Counter(s1)
        window = Counter()
        counter = 0

        # In this case, we need to work in a fixed sliding window,
        # so, we create and process our first window
        for r in range(n):
            # If s2[r] is in s1_counter, and there are not remaining letters,
            # after increment window[s2[r]], then, increment counter
            if s2[r] in s1_counter:
                window[s2[r]] += 1
                if window[s2[r]] <= s1_counter[s2[r]]:
                    counter += 1
        
        # If counter = n, that means we have teh same amount of characters than s1,
        # and, we have the same frequencies in the same characters.
        if counter == n: return True

        # If the first window is not a permutation of s1, we keep visiting s2
        l = 0
        for r in range(n,m):
            if s2[r] in s1_counter:
                window[s2[r]] += 1
                if window[s2[r]] <= s1_counter[s2[r]]:
                    counter += 1

            # The difference here is, before decrement s2[l] in window,
            # we need to know if there are remaining letters in window[s2[l]].
            # If there aree remaining letters, we dont need to decrement counter,
            # because we could need one from this remaining letters in the future.
            # Otherwise, decrement counter.
            # Then, decrement window[s2[l]]
            if s2[l] in s1_counter:
                if window[s2[l]] <= s1_counter[s2[l]]:
                    counter -= 1
                window[s2[l]] -= 1
            l += 1
            if counter == n: return True
        return False
            

            


            

        
        

        
        