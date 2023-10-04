class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        length = len(nums)
        counter = 0
        for i in range(1, length + 1):
            if length % i == 0:
                counter += (nums[i - 1] ** 2)
        return counter

