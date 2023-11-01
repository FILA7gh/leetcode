class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        new_n = ''
        counter = 0
        for i in n:
            if counter > 0 and counter % 3 == 0:
                new_n += '.'
            new_n += i
            counter += 1
        return new_n[::-1]
