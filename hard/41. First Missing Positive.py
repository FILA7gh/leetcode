class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        dct = {}
        for i in nums:
            dct[i] = 1
        max_num = max(nums)
        if max_num <= 0:
            return 1
        for i in range(1, max_num):
            if not dct.get(i):
                return i
        return max_num + 1
