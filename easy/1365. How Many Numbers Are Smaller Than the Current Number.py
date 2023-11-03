class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        some_list = []
        for i in nums:
            counter = 0
            for k in nums:
                if i > k:
                    counter += 1
            some_list.append(counter)
        return some_list
