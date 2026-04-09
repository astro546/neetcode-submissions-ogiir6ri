class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #First, sort the array 
        #Now, since i have the sorted array, i can iterate the array to check directly if there is a consecutive numbers sequence
        if len(nums) == 0 or len(nums) == 1: return len(nums)

        nums.sort()
        count = 0
        max_count = 0
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                count += 1
            elif nums[i+1] == nums[i]:
                if count > max_count:
                    max_count = count

            else:
                count = 0

            if count > max_count:
                max_count = count

        return max_count + 1