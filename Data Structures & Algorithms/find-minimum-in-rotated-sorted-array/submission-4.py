class Solution:
    # O 
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        min = nums[r]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < min:
                min = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return min
        