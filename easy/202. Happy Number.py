class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            summa = 0
            for i in str(n):
                summa += int(i) ** 2
            n = summa
            if n == 4:
                return False
        return True
