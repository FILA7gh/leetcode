class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        my_dict = {}
        for i in nums:
            if my_dict.get(i):
                my_dict[i] = 2
                continue
            my_dict[i] = 1

        for key, value in my_dict.items():
            if value == 1:
                return key
