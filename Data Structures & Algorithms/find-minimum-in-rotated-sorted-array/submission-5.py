class Solution:
    # O(log n)
    # The criteria to search the minimum with binary search is:
    # 1.- Define the left and right boundaries: l = 0, r = len(nums) - 1
    # 2.- Define the default minimum: min = nums[r]
    # 3.- while l <= r, do 4 and 5:
    # 4.- If nums[mid] < min, then the new min is nums[mid] and move to the left
    # 5.- If not, move to the right
    # 6.- Once the loop finishes, return min
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
        