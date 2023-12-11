class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_price = 0

        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        return max_price
