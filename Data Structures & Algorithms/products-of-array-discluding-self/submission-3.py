class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n), but this solution is the best, because no performs divisions (division is slower than a product),
        #and has automatic handle of zeros
        #prefix is the product of all nums before i
        #postfix is the product of all nums after i
        #In both cases, i is not into the product
        prefix = 1
        postfix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
