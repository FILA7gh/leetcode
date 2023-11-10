class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        sub_sum = []
        for i in nums:
            sub_sum.append(nums.pop(nums.index(max(nums))))
            nums.append(0)
            print(sub_sum)
            if sum(sub_sum) > sum(nums):
                return sub_sum
