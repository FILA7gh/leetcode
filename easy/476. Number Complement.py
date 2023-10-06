class Solution:
    def findComplement(self, num: int) -> int:
        new_num = bin(num)[2:]
        nbin = ''
        for i in new_num:
            nbin += '0' if i == '1' else '1'

        return int(nbin, 2)
    