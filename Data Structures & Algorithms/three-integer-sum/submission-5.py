class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0: break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + num
                if curr_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res

            
            

        