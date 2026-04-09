class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_zeros = 0
        zero_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
                zero_idx = i
            elif num_zeros <= 1:
                prod *= nums[i]

        if num_zeros >= 1:
            res = [0] * len(nums)
            if num_zeros == 1:
                res[zero_idx] = prod
                return res
            else:
                return res
        
        else:
            res = []
            for num in nums:
                res.append(prod//num)
            return res

