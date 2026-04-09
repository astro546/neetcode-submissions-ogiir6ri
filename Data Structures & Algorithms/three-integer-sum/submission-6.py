class Solution:
    # Time: O(n^2),
    # Space: O(n) for the sorting algorithm, where n = len(nums)
    # O(m) for the result array, where m = len(res)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, sort the nums array to get first the negative numbers
        res = []
        nums.sort()
        
        # Iterate the sorted array, and for each iteration:
        for i, num in enumerate(nums):
            # If we found a positive number, the following numbers will be positive too
            # so, the sum of positive numbers will be always greater than 0,
            # so, break the cycle
            if num > 0: break

            # if i is not the start of the array and the previuos number is the same as the current number,
            # continue to the following steps
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Perform a two pointers with opposite directions algorithm into the rest of the array,
            # were we will check if the values of l and r plus the current number is 0
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + num
                # If the current sum is 0, append the triplet to the result array,
                # move the pointers and move l if there are duplicates from the left
                if curr_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                # If the current sum is positive, move r, else, move l
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res

            
            

        