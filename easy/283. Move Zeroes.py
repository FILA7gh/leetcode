class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loop = 0
        index = 0
        while loop != len(nums):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                index -= 1
            index += 1
            loop += 1
