class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        week = 1
        total = 0
        money = 1

        while day != n:
            total += money
            day += 1
            money += 1
            if day % 7 == 0:
                week += 1
                money = week

        return total
