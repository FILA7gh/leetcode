# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         group = []
#         for i in range(len(strs)):
#             inside_group = []
#             for k in range(len(strs)):
#                 if sorted(strs[i]) == sorted(strs[k]):
#                     inside_group.append(strs[k])
#             if inside_group not in group:
#                 group.append(inside_group)
#         return group
