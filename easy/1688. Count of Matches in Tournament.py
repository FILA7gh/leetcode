class Solution:
    def numberOfMatches(self, n: int) -> int:
        counter = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
                counter += n
            else:
                n = ((n - 1) / 2) + 1
                counter += n - 1

        return counter
