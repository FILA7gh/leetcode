class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums_dict = {i: 1 for i in nums}

        while nums_dict:
            max_elem = max(nums_dict)
            if nums_dict.get(max_elem - max_elem * 2):
                return max_elem
            del nums_dict[max_elem]
        return -1
