class Solution:
    #O(n)
    #This solution works in a set version of the input array
    #FOr each number in the set, verify if is the start number of a consecutive sequence
    #If is, check for every consecutive number if it is in the array, until the last consecutive array will not in the array
    #after that, updates max_count if length > max_count}
    #When the for loop finishes, return max_count
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max_count = 0
        length = 1
        for n in numsSet:
            if n - 1 not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                max_count = max(max_count, length)
        return max_count
        