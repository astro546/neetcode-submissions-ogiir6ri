class Solution:
    # Time: O(n), Space: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf') # Acts as your 's' pointer tracking the lowest dip
        
        for price in prices: # 'price' acts as your 'f' pointer
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
                    
        return max_profit