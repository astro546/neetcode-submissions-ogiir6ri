class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # 3.-
        word_freqs = {}
        for i in range(len(s)):
            word_freqs[s[i]] = 1 + word_freqs.get(s[i], 0)
            word_freqs[t[i]] = word_freqs.get(t[i], 0) - 1

        for char, freq in word_freqs.items():
            if freq != 0:
                return False


        #2.-
        #word_freqs = {}
        #for i in s:
        #    word_freqs[i] = 1 + word_freqs.get(i, 0)

        #for j in t:
        #    if j not in word_freqs:
        #        return False

        #    word_freqs[j] -= 1
        #    if word_freqs[j] < 0:
        #        return False

        #for char, freq in word_freqs.items():
        #    if freq > 0:
        #        return False

        return True

        #1.-
        #temp = set(s)
        #index = 0
        #for char in temp:
        #    if char in t:
        #        print(char, t)
        #        index += 1;
        
        #if index == len(temp): return True
        #return False