class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 1):
            for k in range(i + 1, len(nums)):
                if nums[i] == nums[k]:
                    count += 1
        return count
    