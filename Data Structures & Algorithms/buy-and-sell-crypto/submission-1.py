class Solution:
    # Time: O(n), Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        # We use a flexible slinding window, 
        # where the left pointer (s), is the buy price, 
        # and the right pointer (f) is the sell price.
        # We update max_profit if the sell price is greater than the buy price,
        # that means we get an amount of money that returns to us after sell a stock
        max_profit = 0
        s = 0
        for f in range(len(prices)):
            profit = prices[f] - prices[s]
            while profit < 0:
                s += 1
                profit = prices[f] - prices[s]

            max_profit = max(max_profit, profit)
        return max_profit