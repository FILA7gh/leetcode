# def garbageCollection(garbage: list[str], travel: list[int]) -> int:
#     counter = 0
#     trucks = ['G', 'P', 'M']
#     for truck in trucks:
#         for i in range(len(garbage)):
#             count = garbage[i].count(truck)
#             if i != 0:
#                 if count:
#                     counter += count
#                 else:
#                     counter -= travel[i-1]
#             elif count and i == 0:
#                 counter += count
#         counter += sum(travel)
#     return counter
#
#
# print(garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
