class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        lst = [i for i in range(len(nums)+1)]
        for i in lst:
            if i not in nums:
                return i
