class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res_list = []
        for i in range(len(nums)//2):
            num1 = nums.pop(nums.index(min(nums)))
            num2 = nums.pop(nums.index(min(nums)))
            res_list.append(num2)
            res_list.append(num1)
        return res_list