class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(s, nums)
        return not (len(s) == len(nums))
        