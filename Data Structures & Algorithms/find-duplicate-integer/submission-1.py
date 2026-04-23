class Solution:
    # Time: O(n), Space: O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        # This code simply iterates the nums array one time,
        # but uses a set to check duplicates
        uniques = set()
        for num in nums:
            if num in uniques:
                return num
                break
            else:
                uniques.add(num)

        