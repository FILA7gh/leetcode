class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        rich_customer = 0
        for rich in accounts:
            richest = sum(rich)
            if richest >= rich_customer:
                rich_customer = richest
        return rich_customer
    