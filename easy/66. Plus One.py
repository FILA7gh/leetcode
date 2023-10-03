class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d = int(''.join(map(lambda x: str(x), digits)))
        d += 1
        ld = []
        for i in str(d):
            ld.append(int(i))
        return ld
