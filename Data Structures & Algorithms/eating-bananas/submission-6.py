class Solution:
    #O(n log m) n = len(piles), m = max(piles)
    # isMinPile verifies if mid is a posible k by acting as a divisor
    # in the sum of 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1: return math.ceil(piles[0] / h)

        def isMinPile(mid: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours <= h:
                return True
            return False

        min_h = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if isMinPile(m):
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

