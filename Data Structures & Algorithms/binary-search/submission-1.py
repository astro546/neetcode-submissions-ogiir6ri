class Solution:
    #O(log n)
    #Binary search works like this:
    #1.- Define left and right bounds (l = 0, r = len(arr) - 1)
    #2.- While the left boundary does not exeed the right boundary, do 3-6 steps:
    #   3.- Calculate m = (l + r) / 2 (or m = l + (r - l) / 2 to prevent integer overflow)
    #   4.- if target = nums[m], that means we have found the target, so, return m
    #   5.- else, if target is less than nums[m], move to the left (r = m - 1)
    #   6.- else, that means target is greater than nums[m], so, move to the right (l = m + 1)
    #7.- If finishes the while loop without return, returns -1
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        