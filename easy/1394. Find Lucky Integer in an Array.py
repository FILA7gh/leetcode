class Solution:
    def findLucky(self, arr: list[int]) -> int:
        set_list = frozenset(arr)
        lucky_list = []
        for i in set_list:
            if i == arr.count(i):
                lucky_list.append(i)
        return lucky_list[-1] if len(lucky_list) > 0 else -1
