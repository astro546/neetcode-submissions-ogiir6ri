class Solution:
    # Time: O(n), Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if f == s:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s

        