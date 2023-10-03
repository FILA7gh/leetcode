class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num1 in range(len(nums)):
            for num2 in range(num1+1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    target_list = [num1, num2]
        return target_list
