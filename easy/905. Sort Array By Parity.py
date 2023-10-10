class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = [x for x in nums if x % 2 == 0]
        m = [x for x in nums if x % 2 == 1]
        n.extend(m)
        return n
