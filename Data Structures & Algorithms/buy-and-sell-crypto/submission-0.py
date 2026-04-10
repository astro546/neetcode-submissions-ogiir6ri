class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        s = 0
        for f in range(len(prices)):
            profit = prices[f] - prices[s]
            while profit < 0:
                s += 1
                profit = prices[f] - prices[s]

            max_profit = max(max_profit, profit)
        return max_profit