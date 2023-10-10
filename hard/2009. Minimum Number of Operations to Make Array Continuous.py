# class Solution:
#     def minOperations(self, nums: list[int]) -> int:
#         min_num = min(nums)
#         max_num = max(nums)
#         length = len(nums) - 1
#         target_nums = range(min_num, min_num + length + 1)
#         target_nums2 = range(max_num - length, max_num + 1)
#         counter2 = 0
#         counter = 0
#         len_set = len(set(nums))
#         if length != len_set:
#             counter += (length + 1) - len_set
#             counter2 = counter
#         for i in nums:
#             if i not in target_nums:
#                 counter += 1
#             if i not in target_nums2:
#                 counter2 += 1
#         return counter if counter < counter2 else counter2
