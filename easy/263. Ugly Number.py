class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        divisor = [2, 3, 5]
        for di in divisor:
            while n % di == 0:
                n //= di
        return n == 1
