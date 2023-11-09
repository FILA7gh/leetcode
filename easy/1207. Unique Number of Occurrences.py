class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        set_list = set(arr)
        count_list = []
        for i in set_list:
            count_list.append(arr.count(i))
        return True if len(count_list) == len(set(count_list)) else False
