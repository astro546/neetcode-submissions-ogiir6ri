class Solution:
    # Time: O(n log n), Space: O(1)
    # This solution use binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # For each number in numbers,
        # Get the difference with the target, 
        # and apply binary search using the difference like the criteria to change the search space
        for i in range(len(numbers)):
            l, r = 0, len(numbers) -1
            dif = target - numbers[i]
            while l <= r:
                m = l + (r - l) // 2
                if dif == numbers[m]:
                    return [i + 1, m + 1]
                elif dif <= numbers[m]:
                    r = m - 1
                else: 
                    l = m + 1
        
        return []