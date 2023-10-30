class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        new_arr = set(arr)
        max_num = arr[0]
        for i in new_arr:
            if arr.count(i) > arr.count(max_num):
                max_num = i
        return max_num
