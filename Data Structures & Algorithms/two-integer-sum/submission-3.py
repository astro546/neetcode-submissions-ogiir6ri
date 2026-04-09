class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i == j: continue
                indexes = [i, j] if i < j else [j, i]
                return indexes

        #1
        #for i in range(len(nums)):
        #   for j in range(len(nums)):
        #        if i == j: continue
        #        if nums[i] + nums[j] == target:
        #            indexes = [i, j] if i < j else [j, i]
        #            return indexes