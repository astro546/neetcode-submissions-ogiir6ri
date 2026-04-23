class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniques = set()
        for num in nums:
            if num in uniques:
                return num
                break
            else:
                uniques.add(num)

        