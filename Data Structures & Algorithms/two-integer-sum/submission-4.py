class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #3
        if len(nums) == 2: return [0,1]

        hash = {value: index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            diff = target - nums[i]
            j = hash.get(diff,-1)
            if j != -1 and i != j:
                indexes = [i, j] if i < j else [j, i]
                return indexes

        #2
        #for i in range(len(nums)):
        #    diff = target - nums[i]
        #    if diff in nums:
        #        j = nums.index(diff)
        #        indexes = [i, j] if i < j else [j, i]
        #        return indexes

        #1
        #for i in range(len(nums)):
        #   for j in range(len(nums)):
        #        if i == j: continue
        #        if nums[i] + nums[j] == target:
        #            indexes = [i, j] if i < j else [j, i]
        #            return indexes