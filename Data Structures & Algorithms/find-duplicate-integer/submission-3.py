class Solution:
    # Time: O(n), Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        # This solution treats the array like a linked list.
        # This works since all numbers inside of the nums array is in the inclusive range [1,n]
        # so, we can treat every number like the index that points to.
        # For example, nums[0] = 1, that means, nums[0] points to index 1
        # Treating the array like a linked list, we can be able to execute the algorithm
        # to detect cycles in a linked list.
        # If we detect that fast and slow pointers are equal, we already found a cycle
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if f == s:
                break

        # After we found a cycle, now, we need the number that produce this cycle.
        # We use slow2 and move it as the same speed as slow,
        # Both pointers will eventually meet together
        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s

        