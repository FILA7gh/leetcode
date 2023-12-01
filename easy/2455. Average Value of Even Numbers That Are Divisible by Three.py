class Solution:
    def averageValue(self, nums: list[int]) -> int:
        nums = [i for i in nums if i % 2 == 0 and i % 3 == 0]
        if nums:
            return sum(nums) // len(nums)
        return 0
