class Solution:
    # Time: O(n), Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            # If the sum of the current values of l and r is equal to target,
            # We found both indexes, so, return the list with both added by 1
            # because the problem asks that it be 1 indexed
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            
            # If the sum is larger than target, move r, else, move l
            if curr_sum > target:
                r -= 1
            else:
                l += 1

        return []
