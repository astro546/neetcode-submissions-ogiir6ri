class Solution:
    # O(log n)
    # If an array is rotated, one half is sorted and one not
    # To know if a half is sorted, the following condition is satisfied: nums[l] < nums[r]
    # In each half, this is translated to: nums[m] <= nums[r] or nums[m] >= nums[l]
    # In the left half, if target is between l and m, move to the left, else, move to the right
    # In the right half, if target is between r and m, move to the right, else, move to the left
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            m = l + (r - l)// 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
            