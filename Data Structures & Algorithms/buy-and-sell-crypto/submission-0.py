class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_seen:
                min_seen = price
            else:
                max_profit = max(max_profit, price - min_seen)
        return max_profit

        