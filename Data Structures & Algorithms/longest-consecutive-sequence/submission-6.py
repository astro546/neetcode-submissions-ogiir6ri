class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(n)
        #This solution uses a hashmap (mp) with the following structure:
        #   n: length, n and legth are int, where n is a num into nums, and length i the legth of the secuence that the number is part of
        #For each number in nums array, if the number is not in the hashmap:
        #then, the value of the new number will be the sum of the legths of its consecutive numbers
        #next, update the length of the left and right boundaries numbers of the sequence that the new number is part of
        #next, update res if the length of the new number is greater than res
        mp = defaultdict(int)
        res = 0
        for n in nums:
            if not mp[n]:
                mp[n] = mp[n - 1] + mp[n + 1] + 1 
                mp[n - mp[n - 1]] = mp[n]
                mp[n + mp[n + 1]] = mp[n]
                res = max(res, mp[n])
        return res

            