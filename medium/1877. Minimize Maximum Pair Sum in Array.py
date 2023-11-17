class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        nums_length = len(nums) // 2
        nums_1 = nums[:nums_length]
        nums_2 = (nums[nums_length:])[::-1]
        max_pairs = 0

        for i in range(nums_length):
            nums_sum = nums_1[i] + nums_2[i]
            if max_pairs < nums_sum:
                max_pairs = nums_sum

        return max_pairs
