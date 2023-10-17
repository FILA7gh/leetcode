class Solution:
    def bitwiseComplement(self, n: int) -> int:
        new_n = ''
        bit = bin(n)[2:]
        print(bit)
        for i in bit:
            new_n += '0' if i == '1' else '1'
        print(new_n)
        return int(new_n, 2)
