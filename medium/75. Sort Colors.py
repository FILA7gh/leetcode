class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        for i in range(len(nums)):
            min_num = min(nums)
            new_min_num = nums.pop(nums.index(min_num))
            new_list.append(new_min_num)
        nums.clear()
        nums.extend(new_list)
    