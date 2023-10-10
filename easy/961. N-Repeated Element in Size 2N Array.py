class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n = len(nums) / 2
        for i in nums:
            i_count = nums.count(i)
            if i_count == n:
                return i
