class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new_list = []
        summ = 0
        for i in nums:
            new_list.append(i + summ)
            summ += i
        return new_list
