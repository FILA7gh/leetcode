# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         permute_list = []
#         for num in range(len(nums)):
#             internal_list = [nums[num]]
#             internal_nums = nums.pop(num)
#             for i in internal_nums:
#                 internal_list.append(i)
#             permute_list.append(internal_list)
#
#         return permute_list
