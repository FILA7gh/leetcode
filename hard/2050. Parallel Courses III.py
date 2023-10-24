# def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:
#     some_dict = {}
#     for i in range(1, n + 1):
#         some_dict[i] = time[i - 1]
#     some_list = []
#
#     while len(relations) > 0:
#         x = relations[0][1]
#         w_list = []
#         w_rel = relations.copy()
#         for i in w_rel:
#             if i[1] == x:
#                 w_list.append(some_dict[i[0]])
#                 relations.pop(relations.index(i))
#         w_rel = relations.copy()
#         some_list.append(max(w_list))
#     return sum(some_list) + some_dict[n]
#
#
# print(minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))
#
#
# #  blyat kogda nibud reshu etu huyny
