class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summa = 0
        mult = 1
        for i in str(n):
            summa += int(i)
            mult *= int(i)
        return mult - summa
