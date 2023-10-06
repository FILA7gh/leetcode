class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_list = []
        if len(prices) < 2:
            return 0
        for price in range(len(prices)-1):
            max_price = max(prices[price + 1:])
            profit = max_price - prices[price]
            profit_list.append(profit)
        max_profit = max(profit_list)
        return max_profit if max_profit > 0 else 0
